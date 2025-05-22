import requests
import unittest

class TestStringMethods(unittest.TestCase):
    
    #Testando POST
    def test_001_POST_reservas(self):
        r = requests.post('http://127.0.0.1:8888/reserva',json={
            "capacidade": 30,
            "data": "10-12-21",
            "id": 1,
            "lab": True,
            "numero_sala": 220,
            "professor_id": 2,
            "turma_id": 1
        })

        r_lista = requests.get('http://127.0.0.1:8888/reserva')
        reservas = r_lista.json()

        reserva_1 = False
        for reserva in reservas:
            if (reserva['data'] == '10-12-21') and (reserva['turma_id'] == 1):
                    reserva_1 = True
            
        if not reserva_1:
            self.fail('Reserva criada foi encontrada.')

    #Testando GET
    def test_002_GET_reservas(self):
        r_lista = requests.get('http://127.0.0.1:8888/reserva')
        reservas = r_lista.json()

        reserva_1 = False
        for reserva in reservas:
            if (reserva['data'] == '10-12-21') and (reserva['turma_id'] == 1):
                    reserva_1 = True
            
        if not reserva_1:
            self.fail('Reserva criada foi encontrada.')

    #Testando DELETE
    def test_003_DELETE_reservas(self):
        r_lista = requests.get('http://127.0.0.1:8888/reserva')
        self.assertEqual(r_lista.status_code, 200)
        reservas = r_lista.json()

        reserva_1 = False
        for reserva in reservas:
            if (reserva['data'] == '10-12-21') and (reserva['turma_id'] == 1):
                    reserva_1 = True
                    reserva_id = reserva["id"]
            
        if not reserva_1:
            self.fail("Reserva não encontrada")
            
        r = requests.delete(f'http://127.0.0.1:8888/reserva/{reserva_id}')
        self.assertEqual(r.status_code, 200)

        reserva_1_encontrada = False
        
        for reserva in reservas:
            if (reserva['data'] == '10-12-21') and (reserva['turma_id'] == 1):
                reserva_1_encontrada = True

        if not reserva_1_encontrada:
            self.fail("Reserva encontrada")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()