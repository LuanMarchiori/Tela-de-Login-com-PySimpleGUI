import PySimpleGUI as sg

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os Eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'user' and valores['senha'] == '123':
            print('Logado')