from dash import html
from dash import dcc

def vias_layout():
    return html.Div([
        html.H1("CONSTRUCIÓN DE VIAS"),
        html.Div([
            html.Label('Tipo de Via', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Via Pavimento Flexible', 'value': 'flexible'},
                    {'label': 'Via Pavimento Rigido', 'value': 'rigido'},
                    {'label': 'Via adoquin', 'value': 'adoquinv'}
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
            dcc.Input(id='p_inicial', type='text', placeholder='(m)')
        ], style={'margin-bottom': '10px'}),  # Establece un margen inferior para separarlo de los demás inputs
        html.Button('Calcular', id='submit-button', n_clicks=0)
    ])
