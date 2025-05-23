📚 API de Reserva de Salas
Este repositório contém a API de Reserva de Salas, desenvolvida com Flask e SQLAlchemy, como parte de uma arquitetura baseada em microsserviços.

🧩 Arquitetura
A API de Reserva de Salas é um microsserviço que faz parte de um sistema maior, o School System, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ Esta API depende de outra API de Gerenciamento Escolar (School System), que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:

Se a Turma existe (GET /turmas/<id>)

Se o Professor existe (GET /turmas/<idProfessor>)

Contagem de Alunos (GET /alunos) — para verificar a quantidade de alunos da turma

🚀 Tecnologias Utilizadas
Python 3.x

Flask

SQLAlchemy

SQLite (como banco de dados local)

Requests (para consumo da API externa)

▶️ Como Executar a API
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/Gustavo-Gozzi/escolaMaster_ReservaSala.git
cd ESCOLAMASTER_RESERVASALA
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a API:

bash
Copiar
Editar
python app.py
A aplicação estará disponível em:
📍 http://localhost:8000

📝 Observação: O banco de dados é criado automaticamente na primeira execução.

📡 Endpoints Principais
GET /reserva — Lista todas as reservas

POST /reserva — Cria uma nova reserva

GET /reserva/<id> — Detalha uma reserva

⚠️ Observação: No código atual não há implementação dos métodos PUT e DELETE para reservas. Apenas os métodos GET (listar e detalhar) e POST (criação) estão disponíveis.

✅ Exemplo de corpo JSON para criação:
json
Copiar
Editar
{
  "turma_id": 1,
  "professor_id": 1,
  "lab": true,
  "numero_sala": "104",
  "data": "2025-04-01",
  "capacidade": 52
}
🔗 Dependência Externa
Certifique-se de que a API de Gerenciamento Escolar esteja rodando em:
📍 http://localhost:8000

E que os endpoints GET /turmas/<id> e GET /alunos estejam funcionando corretamente para que a validação e a contagem de alunos sejam realizadas com sucesso.

📦 Estrutura do Projeto
pgsql
Copiar
Editar
reserva-salas/
│
├── app.py
├── reserva_model.py
├── database.py
├── routes.py
├── requirements.txt
└── README.md
🛠️ Futuras Melhorias
Implementação de atualização (PUT) e remoção (DELETE) de reservas

Validação de conflito de horário na sala

Integração via fila (RabbitMQ) com outros microsserviços

Autenticação de usuários

🧑‍💻 Autores
Este projeto foi desenvolvido de forma colaborativa por:

Daniel

Guilherme

Gustavo

João Vitor

Mikael

Projeto educativo de arquitetura com Flask e microsserviços.