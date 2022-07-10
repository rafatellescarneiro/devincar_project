import json
from typing import Dict, Any, List
from app.menu.design import MenuDesign

class LocalDatabase:

    @staticmethod
    def normalize_data(parameters: List, data: List)-> Dict[str, Any]:
        return dict(zip(parameters, data))
    
    @staticmethod
    def select(file_path: str, entity_name: str):
        try:
            print()
            MenuDesign.made_terminal_component(f"{entity_name.upper()}'TABLE'", fill_char="#")
            with open(file_path, "r+") as file:
                file_data = json.load(file)
                colunas = list(file_data[entity_name][0].keys())
                qtd_colunas = len(colunas)
                qtd_linhas = len(file_data[entity_name])
                matriz = [colunas]
                for i in range(qtd_linhas):
                    linha = []
                    for j in range(qtd_colunas):
                        linha.append(list(file_data[entity_name][i].values())[j])
                    matriz.append(linha)
                for i in range(qtd_linhas + 1):
                    for j in range(qtd_colunas):
                        print(f"{matriz[i][j]}       ", end=" ")
                    print()
            print()
        except FileNotFoundError as exception:
            print(f"[ERROR] Dados referente a {entity_name} não existem")

    @staticmethod
    def insert(file_path: str, entity_name: str, data: Dict[str, Any]):
        try:
            with open(file_path, "r+") as file:
                file_data = json.load(file)
                file_data[entity_name].append(data)
                file.seek(0)
                json.dump(file_data, file)
            print(f"[INFO] Dados de {entity_name} salvos no diretório data/\n")
        except FileNotFoundError as exception:
            print(f"\n[INFO] Arquivo de {entity_name} não Encontrado")
            print(f"[INFO] Criando arquivo ...")
            base = {entity_name: []}
            with open(file_path, "w") as file:
                json.dump(base, file)
            LocalDatabase.insert(file_path, entity_name, data)
        except Exception as exception:
            return exception

