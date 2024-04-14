from dash import html
from dash import dcc

def tuberias_layout():
    return html.Div([
        html.H1("Instalacion tuberias"),
        html.Div([
            html.Label('Sistema', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Alcantarillado pluvial', 'value': 'pluvial'},
                    {'label': 'Sanitaria', 'value': 'sanitaria'},
                    {'label': 'Acueducto', 'value': 'acueducto'}
                ],
                value='Elige el sistema',
                style={'width': '300px'}
            )
        ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),  # Establece un margen inferior para separarlo de los inputs
        html.Div([
            html.Label('Logitud'),
            dcc.Input(id='logitud', type='text', placeholder='Logitud')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Diametro'),
            dcc.Input(id='diametro', type='text', placeholder='Diametro')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Profundidad inicial'),
            dcc.Input(id='p_inicial', type='text', placeholder='(m)')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Profundidad finalk'),
            dcc.Input(id='p_final', type='text', placeholder='(m)')
        ], style={'margin-bottom': '10px'}),
        html.Button('Enviar', id='submit-button', n_clicks=0)
    ])
