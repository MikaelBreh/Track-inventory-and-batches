from PySimpleGUI import PySimpleGUI as sg
from general.layout import login_window


def login():
    # Criar a janela inicial de login
    janela1 = login_window()

    # Criar loop para leitura de eventos
    while True:
        window, event, values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            return False
            break

        user = 0
        if event == 'Entrar':
            if values['usuario'] == '' and values['senha'] == '':
                print('Voce fez o login com sucesso!')
                user = 1  # Admin User
                break
            elif values['usuario'] == 'fabiane' and values['senha'] == '':
                print('Voce fez o login com sucesso!')
                user = 2  # Fabi User
                break
            elif values['usuario'] == 'rian' and values['senha'] == '':
                print('Voce fez o login com sucesso!')
                user = 3  # Rian User
                break
            else:
                janela1['texto_usuario'].update('usuario ou senha incorretos!')


    janela1.close()
    return user