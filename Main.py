from PySimpleGUI import PySimpleGUI as sg
from general.login import login
from general.main_menu import main_menu


login_situation = login()
print(login_situation)

if login_situation is not False:
    opcao_menu = main_menu(login_situation)

    while opcao_menu is not False:
        print('aberto')

        # Abrir página do menu conforme escolha do usuario
        if opcao_menu == 'Lançar entrada de pedidos':
            print('Lançar entrada de pedidos')





        opcao_menu = main_menu()