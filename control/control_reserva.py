from flask import Blueprint, request, jsonify
from model import model_reserva
from database import db
import requests

routes = Blueprint("routes", __name__)

def validar_turma(idTurma):
    turma = requests.get(f"http://localhost:8000/turmas/{idTurma}")
    return turma.status_code == 200

def validar_professor(idProfessor):
    professor = requests.get(f"http://localhost:8000/turmas/{idProfessor}")
    return professor.status_code == 200

def contar_alunos(idTurma):
    alunos = requests.get(f"http://localhost:8000/alunos")
    json_alunos = alunos.json()
    
    contador = 0
    for aluno in json_alunos:
        if aluno["turma_id"] == idTurma:
            contador += 1

    return contador


@routes.route("/reserva", methods=["POST"])
def reservarSala():
    dados = request.json
    idTurma = dados.get("turma_id")
    idProfessor = dados.get("professor_id")
    numeroSala = dados.get("numero_sala")
    reservaData = dados.get("data")
    capacidadeSala = dados.get("capacidade")

    if not validar_professor(idProfessor):
        return jsonify("Professor não encontrado"), 200


    if validar_turma(idTurma):
        reservas = model_reserva.Reserva.query.all()
        for reserva in reservas:
            if reserva.turma_id == idTurma and reserva.data == reservaData:
                return jsonify(f"A turma {idTurma} já possui reserva no dia {reservaData}."), 400
            
            if reserva.professor_id == idProfessor and reserva.data == reservaData:
                return jsonify(f"Este professor já está com uma reserva no dia {reservaData}."), 400
            
            if reserva.numero_sala == numeroSala and reserva.data == reservaData:
                return jsonify(f"A sala {numeroSala} já está ocupada no dia {reservaData}."), 400
 
        contador = contar_alunos(idTurma)
        if contador > capacidadeSala:
            return jsonify(f"A quantidade de alunos excedeu a capacidade da Sala. Max: {capacidadeSala}. Excedentes: {contador - capacidadeSala}."), 400

        reserva = model_reserva.Reserva(
            turma_id=idTurma,
            professor_id=idProfessor,
            lab=dados.get("lab"),
            numero_sala=numeroSala,
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
    lista = []
    for reserva in reservas:
        lista.append({
            "id": reserva.id,
            "turma_id": reserva.turma_id,
            "professor_id": reserva.professor_id,
            "numero_sala": reserva.numero_sala,
            "lab": reserva.lab,
            "data": reserva.data,
            "capacidade": reserva.capacidade
        })

    return jsonify(lista), 200


@routes.route("/reserva/<int:idReserva>", methods=["DELETE"])
def deleteReserva(idReserva):
    try:
        reserva = model_reserva.Reserva.query.get(idReserva)
        db.session.delete(reserva)
        db.session.commit()
        return {"msg": "Reserva deletada com sucesso!"}, 200
      
    except:
        return  {"msg":"Professor não encontrado"}, 400


@routes.route("/reserva/<int:idReserva>", methods=["GET"])
def getReservaById(idReserva):
    reserva = model_reserva.Reserva.query.get(idReserva)
    try:
        reservas = {
            "id": reserva.id,
            "turma_id": reserva.turma_id,
            "professor_id": reserva.professor_id,
            "numero_sala": reserva.numero_sala,
            "lab": reserva.lab,
            "data": reserva.data,
            "capacidade": reserva.capacidade
        }

        return jsonify(reservas), 200
    
    except:
        return jsonify("Reserva não encontrada :/"), 400

