from uuid import uuid4
from typing import Dict, Any
from datetime import datetime


from app.entities.database import LocalDatabase
from app.core.config import settings

class Veiculos: 

    def __init__(self)-> None:

        self.chassiNumber = str(uuid4())
        self.__dataFabricacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__nome = None
        self.__placa = None
        self.__valor = None
        self.__cpfComprador = 0
        self.__cor = None
        self.__vendido = False
        self.__parameters = ["chassiNumber", "dataFabricacao", "nome", "placa", "valor", "cpfComprador", "cor", "vendido"]
        self.__list_data = None
        self.__veiculos_file_path = settings.VEICULOS_DATA_PATH
        self.__entity_name = "veiculos"
        

    def listar_todos(self):
        LocalDatabase.select(file_path=self.__veiculos_file_path,
                             entity_name=self.__entity_name)


    def vender_veiculo(self):
        
        self.__cpfComprador = str(input("Digite o CPF do Comprador: "))
        self.__vendido = True
        self.list_data = [
                            self.__chassiNumber, self.__dataFabricacao, self.__nome,
                            self.__placa, self.__valor, self.__cpfComprador, self.__cor, self.__vendido
                        ]
        self.salvar_venda()

    def salvar_venda(self):
        LocalDatabase.insert(file_path=self.__veiculos_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parameters,
                                                               self.__list_data))


        