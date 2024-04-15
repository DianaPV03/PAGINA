from dash import html
from dash import dcc

def espacio_layout():
    return html.Div([
        html.H1("ESPACIO PUBLICO"),
        html.Div([
            html.Label('Selecione el Espacio', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Andenes en adoquin', 'value': 'adoquna'},
                    {'label': 'Andenes en concreo', 'value': 'concre'},
                    {'label': 'Andenes tipo IDU', 'value': 'IDU'}
                ],
                value='Elige el sistema',
                style={'width': '300px'}
            )
        ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),  # Establece un margen inferior para separarlo de los inputs
        html.Div([
            html.Label('Logitud'),
            dcc.Input(id='logitud', type='text', placeholder='(m)')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Ancho'),
            dcc.Input(id='Ancho', type='text', placeholder='Ancho')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Button('Calcular', id='submit-button', n_clicks=0)
    ])
