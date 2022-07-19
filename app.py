import PySimpleGUI as sg
from Conversor import Conversor

sg.theme('PythonPlus')
calculo = Conversor(0)
unidades = calculo.unidades

layout = [
    [sg.Text('CONVERSOR DE UNIDADES', font=('Arial', 16))],
    [sg.HorizontalSeparator()],
    [sg.Text('valor', size=(12,1)), sg.Text('unidade')],
    [sg.Input('1', size=(12,1), key='-input-'),
     sg.Combo(unidades, size=(5,1), key='-unidades-', default_value='mm'),
     sg.Button('CONVERTER')],
    [sg.Multiline('', size=(40, 6), key='-output-')]
]

janela = sg.Window('CONVERSOR DE UNIDADES', layout)

while True:
    evento, valores = janela.read()
    
    if evento == sg.WINDOW_CLOSED:
        break
    if evento in 'CONVERTER':
        unidade = valores['-unidades-']
        entrada = float((valores['-input-']).replace(',','.'))

        janela['-output-'].update(
            calculo.conversor(
                unidade, entrada).upper().replace('.',','))

janela.Close()