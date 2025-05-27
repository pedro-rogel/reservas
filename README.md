**📚 API de Reserva de Salas**

Esta API faz parte da arquitetura de microsserviços do *School System* e é responsável pelo gerenciamento de reservas de salas por turma.

---

## 🧩 Arquitetura

* Microssserviço independente de **Reserva de Salas**
* Comunicação com a API de Gerenciamento Escolar via HTTP REST para validações:

  * **GET** `/turmas/<id>` – Verifica se a Turma existe

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Flask**
* **SQLAlchemy**
* **SQLite** (banco de dados local)
* **Requests** (para consumo da API externa)

---

## ▶️ Como Executar a API

1. **Clone o repositório**

   ```bash
   git clone https://github.com/pedro-rogel/reserva-salas.git
   cd reserva-salas
   ```

2. **Crie um ambiente virtual (recomendado)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a API**

   ```bash
   python run.py
   ```

   A aplicação estará disponível em: **[http://localhost:5000](http://localhost:5000)**

> 📝 **Observação:** O banco de dados `reservas.db` é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

| Método | Rota             | Descrição                   |
| ------ | ---------------- | --------------------------- |
| GET    | `/reservas`      | Lista todas as reservas     |
| POST   | `/reservas`      | Cria uma nova reserva       |
| GET    | `/reservas/<id>` | Detalha uma reserva por ID  |
| PUT    | `/reservas/<id>` | Atualiza uma reserva por ID |
| DELETE | `/reservas/<id>` | Remove uma reserva por ID   |

**Exemplo de corpo JSON para criação/atualização:**

```json
{
  "turma_id": 1,
  "sala": "10A",
  "data": "2025-05-06",
  "hora_inicio": "9:00",
  "hora_fim": "12:00"
}
```

---

## 🔗 Dependência Externa

* Certifique-se de que a API de Gerenciamento Escolar (*School System*) esteja rodando em:

  ```
  http://localhost:9090
  ```

---

## 📦 Estrutura do Projeto

```
reserva/
│
├── app/               # Pacote da aplicação Flask
├── .gitignore         # Arquivos e pastas ignorados
├── config.py          # Configurações da aplicação
├── dockerfile         # Definições para container Docker
├── README.md          # Documentação do projeto
├── requirements.txt   # Dependências do projeto
└── run.py             # Script de inicialização
```

---

## 🛠️ Futuras Melhorias

* Criação do Swagger Completo
* Tratamento de exeções e erros

---

## 🧑‍💻 Autor

**Grupo 5** – Projeto educativo de arquitetura com Flask e microsserviços.
*Pedro Rogel*
*Murillo Perajon*
*Felippe Pereira*
*Gustavo Rodrigues*
*Fernando Barreto*

