from app.core.config import settings
from app.menu.design import MenuDesign
from app.entities import Veiculos, Transferencias, Carro, Moto_Triciclo, Camionete

class MainMenu:

    @staticmethod
    def start():

        while True:
            MenuDesign.made_terminal_component(settings.NOME_SISTEMA, fill_char="=")
            MenuDesign.made_terminal_component("\n1 - Veículos "
                                               "\n2 - Transferências "
                                               "\n3 - Relatórios "
                                               "\n\n0 - Sair\n", fill_char=" ")
            MenuDesign.made_terminal_component("|", fill_char="=")
            opt = int(input("\nSelecione a opção desejada: "))
            MenuDesign.made_terminal_component("|")
            if opt == 1:
                MenuDesign.made_terminal_component("VEICULOS ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Carros \n2 - Motos/Triciclos \n3 - Camionete "
                                                   "\n\n0 - Sair\n", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_opt = int(input("\nSelecione a opção desejada: "))
                MenuDesign.made_terminal_component("|")
                if sub_opt == 1:
                    MenuDesign.made_terminal_component("Carros ", fill_char="=")
                    MenuDesign.made_terminal_component("\n1 - Vender \n2 - Listar \n3 - Editar", fill_char=" ")
                    MenuDesign.made_terminal_component("|", fill_char="=")
                    sub_opt3 = int(input("\nSelecione a opção desejada: "))
                    MenuDesign.made_terminal_component("|")
                    if sub_opt3 == 1:
                        Carro().vender_veiculo()
                    elif sub_opt3 == 2:
                        Carro().listar_todos()
                    elif sub_opt3 == 3:
                        Carro().alterar_info()
                    else:
                        break
                elif sub_opt == 2:
                    MenuDesign.made_terminal_component("Moto/Triciclo ", fill_char="=")
                    MenuDesign.made_terminal_component("\n1 - Vender \n2 - Listar \n3 - Editar", fill_char=" ")
                    MenuDesign.made_terminal_component("|", fill_char="=")
                    sub_opt4 = int(input("\nSelecione a opção desejada: "))
                    MenuDesign.made_terminal_component("|")
                    if sub_opt4 == 1:
                        Moto_Triciclo().vender_veiculo()
                    elif sub_opt4 == 2:
                        Moto_Triciclo().listar_todos()
                    elif sub_opt4 == 3:
                        Moto_Triciclo().alterar_info()
                    else:
                        break
                elif sub_opt == 3:
                    MenuDesign.made_terminal_component("Camionete ", fill_char="=")
                    MenuDesign.made_terminal_component("\n1 - Vender \n2 - Listar \n3 - Editar", fill_char=" ")
                    MenuDesign.made_terminal_component("|", fill_char="=")
                    sub_opt4 = int(input("\nSelecione a opção desejada: "))
                    MenuDesign.made_terminal_component("|")
                    if sub_opt4 == 1:
                        Camionete().vender_veiculo()
                    elif sub_opt4 == 2:
                        Camionete().listar_todos()
                    elif sub_opt4 == 3:
                        Camionete().alterar_info()
                    else:
                        break
                    Camionete()
                else:
                    break
            elif opt == 2:
                MenuDesign.made_terminal_component("TRANSFERENCIAS ", fill_char="=")
                Transferencias().listar_transferencias()

            elif opt == 3:
                MenuDesign.made_terminal_component("RELATÓRIOS ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Listagem de Veículos \n2 - Veículos Disponíveis \n3 - Veículos Vendidos \n4 - Vendido com o maior preço" 
                                                    "\n5 = Vendido com o menor preço \n0 - Sair", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_opt2 = int(input("\nSelecione a opção desejada: "))
                MenuDesign.made_terminal_component("|")
                if sub_opt2 == 1:
                    Veiculos().listar_todos()
                elif sub_opt2 == 2:
                    Veiculos().listar_disponiveis()
                elif sub_opt2 == 3:
                    Veiculos().listar_vendidos()
                elif sub_opt2 == 4:
                    Veiculos().listar_maiorpreco()
                elif sub_opt2 == 5:
                    Veiculos().listar_menorpreco()
                else: break

            elif opt == 0:
                break
                                                           
            else:
                MenuDesign.made_terminal_component("Opção inválida, tente novamente", 80, "#")
