from layout import layout
from callbacks import register_Callback
from flask import Flask
import dash


def create_app():
    server = Flask(__name__)
    app = dash.Dash(
        __name__,
        server=server,
        external_stylesheets=[
            "https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
        ],
    )
    #app.config.suppress_callback_exceptions = True
    app.layout = layout
    register_Callback(app)
    return server, app
