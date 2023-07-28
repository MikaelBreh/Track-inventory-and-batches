from PySimpleGUI import PySimpleGUI as sg
from general.layout import main_menu_window


# funcao para abrir menu principal e executar funcoes
def main_menu(login_situation):
    # criando janela do menu principal - com base no import do layout
    janela = main_menu_window()

    if login_situation == 2:
        janela['Lançar entrada de pedidos'].update(disabled=True)

    if login_situation == 3:
        janela['Lançar entrada de pedidos'].update(disabled=True)


    # Criar loop para leitura de eventos
    while True:
        window, event, values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            return False
            break

        # Se usuario tiver clicado em lancar entrada pedido:
        if event == 'Lançar entrada de pedidos':
            janela.close()
            return 'Lançar entrada de pedidos'



    janela.close()