import dash
from dash.dependencies import Input, Output, State
from dash import html
import tuberias, espacio, vias

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Aplicación Principal"),
    html.Button('Instalación de Tuberías', id='go-to-form-button-tuberias', style={'margin-right': '10px'}),
    html.Button('Espacio Público', id='go-to-form-button-espacio', style={'margin-right': '10px'}),
     html.Button('Vias', id='go-to-form-button-vias', style={'margin-right': '10px'}),
    html.Div(id='form-container')
], style={'display': 'inline-block'})

# Callbacks para mostrar los formularios cuando se hace clic en los botones
@app.callback(
    Output('form-container', 'children'),
    [Input('go-to-form-button-tuberias', 'n_clicks'),
     Input('go-to-form-button-vias', 'n_clicks'),
     Input('go-to-form-button-espacio', 'n_clicks')],
    [State('form-container', 'children')]
)
def display_form(tuberias_clicks, espacio_clicks, vias_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    tuberias_form = tuberias.tuberias_layout() if button_id == 'go-to-form-button-tuberias' else None
    vias_form = vias.vias_layout() if button_id == 'go-to-form-button-vias' else None
    espacio_form = espacio.espacio_layout() if button_id == 'go-to-form-button-espacio' else None

    return [
        tuberias_form,
        vias_form,  
        espacio_form
    ]
if __name__ == '__main__':
    app.run_server(debug=True)
