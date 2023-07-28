from PySimpleGUI import PySimpleGUI as sg


# Standardize text
fonte = ('Helvetica', 16)
fonte_box = ('Helvetiva', 15)
fonte_button = ('Helvetiva', 13)


def login_window():
    sg.theme('Reddit')  # É possivel colocar outros temas (doc. oficial)
    layout = [
        [sg.Text('Usuario', font=fonte), sg.Input(key='usuario', font=fonte_box)],
        [sg.Text('Senha', font=fonte), sg.Input(key='senha', password_char='*', font=fonte_box)],
        [sg.Button('Entrar', font=fonte_button), sg.Button('Cancelar', font=fonte_button)],
        [sg.Text(key='texto_usuario', font=fonte_button)]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def main_menu_window():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Lançar entrada de pedidos', font=fonte_button, size=(10, 2))],
        [sg.Button('Controle de estoque', font=fonte_button, size=(10, 2))],
        [sg.Button('Rastreamento de lotes', font=fonte_button, size=(10, 2))],
        [sg.Button('Cancelar', font=fonte_button)]
    ]
    return sg.Window('Menu Principal', layout=layout, finalize=True)
