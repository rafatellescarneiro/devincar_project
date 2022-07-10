from os.path import abspath, join, dirname


class Settings:

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))

    DATA_PATH = join(ROOT_PATH, "data")

    VEICULOS_DATA_PATH = join(DATA_PATH, "veiculos.json")
    CARRO_DATA_PATH = join(DATA_PATH, "carro.json")
    MOTO_TRICICLO_DATA_PATH = join(DATA_PATH, "moto_triciclo.json")
    CAMIONETE_DATA_PATH = join(DATA_PATH, "camionete.json")
    TRANSFERENCIAS_DATA_PATH = join(DATA_PATH, "transferencias.json")

    NOME_SISTEMA = "SISTEMA DE ARMAZENAMENTO DE INFORMAÇÕES - SAI - DEVinCar"