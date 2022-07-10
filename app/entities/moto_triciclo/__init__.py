
from app.entities.veiculos import Veiculos
from app.entities.database import LocalDatabase
from app.core.config import settings
from app.core import execution_time

class Moto_Triciclo(Veiculos):

    def __init__(self):
        super().__init__()
        self.__rodas = [2, 3]
        self.__potencia = ["110 cv", "130 cv", "165 cv"]
        self.__parameters = ["chassiNumber", "dataFabricacao", "nome", "placa", "valor", "cpfComprador", "cor", "rodas", "potencia"]
        self.__moto_triciclo_file_path = settings.MOTO_TRICICLO_DATA_PATH
        self.__entity_name = "moto_triciclo"
    
    @execution_time
    def listar_moto_triciclo(self):
        LocalDatabase.select(file_path= self.__moto_triciclo_file_path, entity_name=self.__entity_name)

    def alterar_info(self) -> None:

        self.__valor = str(input("Informe o novo valor: "))
        self.__cor = str(input("Informe a nova cor da Moto/Triciclo: "))
        self.__list_data = [self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__potencia, self.__rodas, self.__cor
                            ]
        self.__salvar_alteracao()

    def vender_veiculo(self):
        
        self.__cpfComprador = str(input("Digite o CPF do Comprador: "))
        self.__vendido = True
        self.list_data = [
                            self.chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__potencia, self.__rodas, self.__cor, self.__vendido
                        ]
        self.__salvar_alteracao()

    def __salvar_alteracao(self)-> None:
        LocalDatabase.insert(file_path=self.__moto_triciclo_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parameters,
                                                               self.__list_data))