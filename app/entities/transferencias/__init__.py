from app.entities.veiculos import Veiculos
from app.core.config import settings
from app.entities.database import LocalDatabase
from datetime import datetime
from app.core import execution_time

class Transferencias:

    def __init__(self) -> None:
        self.__veiculos = Veiculos()
        self.__cpfComprador = 0
        self.__valor = None
        self.__data = datetime.now().strftime("%d%m%Y %H:%M:%S")
        self.__parameters = ["chassiNumber", "dataFabricacao", "nome", "placa", "valor", "cpfComprador", "cor", "veiculo", "data"]
        self.__list_data = None
        self.__transferencias_file_path = settings.TRANSFERENCIAS_DATA_PATH
        self.__entity_name = "transferencias"

    @execution_time
    def listar_transferencias(self):
        LocalDatabase.select(file_path=self.__transferencias_file_path,
                            entity_name=self.__entity_name)
        self.__veiculos.listar_todos()
        self.__list_data = [
                            self.__chassiNumber, self.__dataFabricacao, self.__nome, 
                            self.__placa, self.__valor, self.__cpfComprador, self.__cor, self.__veiculo, 
                            self.__data
                            ]
        self.__salvar_alteracao()

    def __salvar_alteracao(self)-> None:
        LocalDatabase.insert(file_path=self.__transferencias_file_path, entity_name=self.__entity_name,
                            data=LocalDatabase.normalize_data(self.__parameters,
                                                            self.__list_data))
