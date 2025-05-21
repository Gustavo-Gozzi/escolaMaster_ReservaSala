from database import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)
    lab = db.Column(db.Boolean, default=False, nullable=False)
    numero_sala = db.Column(db.Integer, nullable=False)
    data = db.Column(db.String(20), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)