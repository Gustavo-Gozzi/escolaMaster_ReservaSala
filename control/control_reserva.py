from flask import Blueprint, request, jsonify
from model import model_reserva
from database import db
import requests

routes = Blueprint("routes", __name__)

def validar_turma(idTurma):
    turma = requests.get(f"http://localhost:8000/turmas/{idTurma}")
    return turma.status_code == 200


@routes.route("/reserva", methods=["POST"])
def reservarSala():
    dados = request.json
    idTurma = dados.get("turma_id")

    if validar_turma(idTurma):
        reserva = model_reserva.Reserva(
            turma_id=idTurma,
            professor_id=dados.get("professor_id"),
            lab=dados.get("lab"),
            numero_sala=dados.get("numero_sala"),
            data=dados.get("data"),
            capacidade=dados.get("capacidade")
        )

        db.session.add(reserva)
        db.session.commit()
        return jsonify("Reserva criada com SUCESSO!"), 200
    
    else:
        return jsonify("Turma não encontrada."), 404

@routes.route("/reserva", methods=["GET"])
def getReserva():
    reservas = model_reserva.Reserva.query.all()
    print(reservas)
    lista = []
    for reserva in reservas:
        lista.append({
            "turma_id": reserva.turma_id,
            "professor_id": reserva.professor_id,
            "lab": reserva.lab,
            "data": reserva.data,
            "capacidade": reserva.capacidade
        })

    return jsonify(lista), 200
