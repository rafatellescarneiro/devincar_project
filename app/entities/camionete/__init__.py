from datetime import datetime

from app.entities.veiculos import Veiculos
from app.entities.database import LocalDatabase
from app.core.config import settings
from app.core import execution_time

class Camionete(Veiculos):

    def __init__(self):
        super().__init__()
        self.__totalPortas = ["2","4"]
        self.__tipoCombustivel = ["Diesel", "Gasolina"]
        self.__capacidade = ["683 lts","1420 lts","1580 lts"]
        self.__potencia = ["225 cv", "234 cv", "258 cv"]
        self.__cor = "Roxa"
        self.__parameters = ["chassiNumber", "dataFabricacao", "nome", "placa", 
                            "valor", "cpfComprador", "totalPortas", "tipoCombustivel", 
                             "capacidade", "potencia", "cor"]
        self.__camionete_file_path = settings.CAMIONETE_DATA_PATH
        self.__entity_name = "camionete"

    @execution_time
    def listar_todos(self):
        LocalDatabase.select(file_path= self.__camionete_file_path, entity_name=self.__entity_name)

    def alterar_info(self) -> None:

        self.__valor = str(input("Informe o novo valor: "))
        print(f"A DEVinCar só fabrica caminhonetes na cor {self.__cor}")
        self.__list_data = [self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__totalPortas, 
                            self.__tipoCombustivel, self.__capacidade, self.__potencia, self.__cor
                            ]
        self.__salvar_alteracao()

    def vender_veiculo(self):
        
        self.__cpfComprador = str(input("Digite o CPF do Comprador: "))
        self.__vendido = True
        self.list_data = [
                            self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__totalPortas, 
                            self.__tipoCombustivel, self.__capacidade, self.__potencia, self.__cor, self.__vendido
                        ]
        self.__salvar_alteracao()

    def __salvar_alteracao(self)-> None:
        LocalDatabase.insert(file_path=self.__camionete_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parameters,
                                                               self.__list_data))