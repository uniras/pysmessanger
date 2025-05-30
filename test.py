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

        # Iframeにクエリーパラメータを使って値を渡すサンプル
        # DashのSliderコンポーネントを使って値を変更する
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


        # pys_messengerを使ってPostMessageで値をやり取りするサンプル
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

        # Iframeから受け取った値を保持するためのStoreコンポーネント
        dcc.Store(id="iframe_data", data=None),
    ]
)


# クエリーパラメータでDashからIframeに値を渡すサンプル
# 非常に手軽だが、値が更新されるたびにIframeがリロードされる、Iframe側からDashに値を返すことができないという制約がある
@app.callback(
    Output("my-iframe", "src"),
    Input("my-slider", "value"),
)
def update_iframe_src(value):
    json_str = json.dumps({"value": value})
    timeparam = time.time()
    return f"/assets/test.html?data={urllib.parse.quote(json_str)}&t={timeparam}"


# pys_messengerを使って値をIframeに送信するサンプル
clientside_callback(
    ClientsideFunction(
        namespace="pys_sender",
        function_name="pys_send",
    ),
    Input("my-iframe2", "id"),
    Input("my-slider2", "value"),
)


# pys_messengerでIframeからデータを受け取りStoreに保存された値をDashコンポーネントに反映するサンプル
@app.callback(
    Output("my-slider2", "value"),
    Input("iframe_data", "data"),
)
def update_slider_value(data):
    if data is None:
        return 50

    return data


app.run(debug=True)
