import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from pages import callgraphs, info, maingraphs

external_stylesheets = [dbc.themes.MINTY]
app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20rem',
    'padding': '2rem 1rem',
    'background-color': '#2642fd'
}

CONTENT_STYLE = {
    'margin-left': '22rem',  # Добавьте отступ слева для основного содержимого
    'padding': '2rem 1rem'
}

sidebar = html.Div(
    [
        html.H2('Клиенты банка', className='display-6', style={'color': 'white'}),
        html.Hr(),
        html.P(
            'Учебный проект студентов БСБО-15-21 Маркешина Б.В. и Корнева А.Е.', className='lead', style={'color': 'white'}
        ),
        dbc.Nav(
            [
                dbc.NavLink('О проекте', href='/', active='exact', style={'color': 'white'}),
                dbc.NavLink('Общие графики', href='/page-1', active='exact', style={'color': 'white'}),
                dbc.NavLink('Информация о звонках', href='/page-2', active='exact', style={'color': 'white'}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id='page-content', style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id='url'), sidebar, content])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/':
        return info.layout
    elif pathname == '/page-1':
        return maingraphs.layout
    elif pathname == '/page-2':
        return callgraphs.layout
    return html.Div(
        [
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f'The pathname {pathname} was not recognised...'),
        ],
        className='p-3 bg-light rounded-3',
    )

if __name__ == '__main__':
    app.run_server(debug=True)
