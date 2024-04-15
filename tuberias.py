from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import app

def tuberias_layout():
    return html.Div([
        html.H1("INSTALACION DE TUBERIAS"),
        html.Div([
            html.Label('Sistema', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Alcantarillado pluvial', 'value': 'pluvial'},
                    {'label': 'Alcantarillado Sanitario', 'value': 'sanitario'},
                    {'label': 'Acueducto', 'value': 'acueducto'}
                ],
                value='Elige el sistema',
                style={'width': '300px'}
            )
        ]),  # Establece un margen inferior para separarlo de los inputs
        html.Div([
            html.Label('Longitud'),
            dcc.Input(id='longitud', type='text', placeholder='(m)')
        ]),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Diametro'),
            dcc.Input(id='diametro', type='text', placeholder='Pulgadas')
        ]),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Profundidad inicial'),
            dcc.Input(id='p_inicial', type='text', placeholder='(m)')
        ]),  # Establece un margen inferior para separarlo de los demás inputs
        html.Div([
            html.Label('Profundidad final'),
            dcc.Input(id='p_final', type='text', placeholder='(m)')
        ]),
        html.Button('Calcular', id='mi-boton', n_clicks=0),
        html.Div(id='mi-output')       
    ])
def callback(app):
    @app.callback(
        Output('mi-output', 'children'),
        [Input('mi-boton', 'n_clicks')],
        [State('longitud', 'value'),
        State('diametro', 'value'),
        State('p_inicial', 'value'),
        State('p_final', 'value')]
    )
    def update_output(n_clicks, longitud, diametro, p_inicial, p_final):
        if n_clicks is not None and n_clicks > 0:
            resultado = calcular_tuberia(float(longitud), float(diametro), float(p_inicial), float(p_final))
            return resultado
        else:
            return ''
    def calcular_tuberia(longitud, diametro, p_inicial, p_final):
        # Aquí puedes realizar tus cálculos
        # Por ejemplo:
        total_tubos = longitud/6
        excavacion = longitud*(diametro*0.0254+0.4)*((p_inicial+p_final)/2)
        resultado_texto = f'Total tubos: {total_tubos}\nExcavacion: {excavacion}'
        return resultado_texto