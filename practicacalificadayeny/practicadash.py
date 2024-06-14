import dash
from dash import dcc,html

app=dash.Dash()

app.layout =html.Div([
    html.H1(children="Datos Generales del área de Plataformas Web"),
    html.Div(children="Gráficos de Datos Comparativos de los aprobados y desaprobados de plataformas web"),
    dcc.Graph(
        id="figura inicial",
           figure={
               "data":[
                   {"x":[1,2,3],"y":[20,27,35],"type":"bar","name":"Datos de los aprobados"},
                   {"x":[1,2,3],"y":[12,18,19],"type":"bar","name":"Datos de los desaprobados"}
               ],
               "layout":{"title":"tabla de los aprobados y desaprobados de Plataformas Web"}
           }
    )  
]
)
if __name__ == "__main__":
    app.run_server(debug=True)