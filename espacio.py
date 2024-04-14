from dash import html
from dash import dcc

def espacio_layout():
    return html.Div([
        html.H1("Espacio publico"),
        dcc.Input(id='input1', type='text', placeholder='Input 1'),
        dcc.Input(id='input2', type='text', placeholder='Input 2'),
        dcc.Input(id='input3', type='text', placeholder='Input 3'),
        html.Button('Enviar', id='submit-button', n_clicks=0)
    ])
