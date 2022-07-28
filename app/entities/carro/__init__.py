from datetime import datetime

from app.entities.veiculos import Veiculos
from app.entities.database import LocalDatabase
from app.core.config import settings
from app.core import execution_time

class Carro(Veiculos):

    def __init__(self):
        super().__init__()
        self.__totalPortas = ['2', '4']
        self.__tipoCombustivel = ["Flex", "Gasolina"]
        self.__potencia = ["192 cv", "206 cv", "231 cv"]
        self.__parameters = ["chassiNumber", "dataFabricacao", "nome", "placa", "valor", "cpfComprador", "cor","totalPortas", "tipoCombustivel", "potencia"]
        self.__carro_file_path = settings.CARRO_DATA_PATH
        self.__entity_name = "carro"

    @execution_time
    def listar_todos(self):
        LocalDatabase.select(file_path= self.__carro_file_path, entity_name= self.__entity_name)

    def alterar_info(self) -> None:

        self.__valor = str(input("Informe o novo valor: "))
        self.__cor = str(input("Informe a nova cor do Carro: "))
        self.__list_data = [self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__totalPortas, 
                            self.__tipoCombustivel, self.__potencia, self.__cor
                            ]
        self.__salvar_alteracao()

    def vender_veiculo(self):
        
        self.__cpfComprador = str(input("Digite o CPF do Comprador: "))
        self.__vendido = True
        self.list_data = [
                            self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__totalPortas, 
                            self.__tipoCombustivel, self.__potencia, self.__cor, self.__vendido
                        ]
        self.__salvar_alteracao()

    def __salvar_alteracao(self)-> None:
        LocalDatabase.insert(file_path=self.__carro_file_path, entity_name=self.__entity_name,
                            data=LocalDatabase.normalize_data(self.__parameters,
                                                            self.__list_data))