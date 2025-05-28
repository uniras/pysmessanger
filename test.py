from dash import Dash, dcc, html, Input, Output, clientside_callback, ClientsideFunction
import urllib
import time
import json
import urllib.parse

# アプリケーションの初期化
app = Dash()

app.layout = html.Div(
    [
        html.H1("スライダーで数値を変更"),
        dcc.Slider(
            id="my-slider",
            min=0,
            max=100,
            step=1,
            value=50,
            marks={i: str(i) for i in range(0, 101, 10)},
        ),
        html.Iframe(
            id="my-iframe",
            src="/assets/test.html?data={}&t=0",
            style={"width": "100%", "height": "300px"},
        ),
        dcc.Slider(
            id="my-slider2",
            min=0,
            max=100,
            step=1,
            value=50,
            marks={i: str(i) for i in range(0, 101, 10)},
        ),
        html.Iframe(
            id="my-iframe2",
            src="/assets/test2.html",
            style={"width": "100%", "height": "300px"},
        ),
        dcc.Store(id="iframe_data", data=None),
        # html.Div(id="dummy-output", style={"display": "none"}),
    ]
)


@app.callback(
    Output("my-iframe", "src"),
    Input("my-slider", "value"),
)
def update_iframe_src(value):
    json_str = json.dumps({"value": value})
    timeparam = time.time()
    return f"/assets/test.html?data={urllib.parse.quote(json_str)}&t={timeparam}"


clientside_callback(
    ClientsideFunction(
        namespace="pys_sender",
        function_name="pys_send",
    ),
    # Output("dummy-output", "children"),
    Input("my-iframe2", "id"),
    Input("my-slider2", "value"),
)


@app.callback(
    Output("my-slider2", "value"),
    Input("iframe_data", "data"),
)
def update_slider_value(data):
    if data is None:
        return 50

    return data


app.run(debug=True)
