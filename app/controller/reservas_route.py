from flask import Blueprint, request, jsonify
from app.model.reservas_model import Reserva
from app import db
import requests

routes = Blueprint("routes", __name__)

def validar_turma(turma_id):
    resp = requests.get(f"https://school-system-hfwh.onrender.com/turmas/{turma_id}")
    return resp.status_code == 200

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")
    
    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400
    
    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )
    
    db.session.add(reserva)
    db.session.commit()
    
    
    return jsonify({"message": "Reserva crida com sucesso"}), 201


@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])
    
@routes.route("/reservas/<int:reserva_id>", methods=["PUT"])
def atualizar_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva:
        return jsonify({"error": "Reserva não encontrada"}), 404
    
    dados = request.get_json()
    
    if "turma_id" in dados:
        if not validar_turma(dados["turma_id"]):
            return jsonify({"erro": "Turma não encontrada"}) 
        reserva.turma_id = dados["turma_id"]
        
    if "sala" in dados:
        reserva.sala = dados["sala"]
    if "data" in dados:
        reserva.data = dados["data"]
    if "hora_inicio" in dados:
        reserva.hora_inicio = dados["hora_inicio"]
    if "hora_fim" in dados:
        reserva.hora_fim = dados["hora_fim"]
    
    
    db.session.commit()
    
    return jsonify({
        "id": reserva.id,
        "turma_id": reserva.turma_id,
        "sala": reserva.sala,
        "data": reserva.data,
        "hora_inicio": reserva.hora_inicio,
        "hora_fim": reserva.hora_fim
    }), 200
    
@routes.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def deletar_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"})
    db.session.delete(reserva)
    db.session.commit()
    
    return jsonify({"message": "Reserva deletada com sucesso"}),200