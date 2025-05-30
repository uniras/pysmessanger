import js  # type: ignore
import json
from pyscript import display  # type: ignore

data = 50


# 許可するPostMessageオリジンのリスト
allow_origin = [js.location.origin]

# すべてのオリジンを許可したい場合(非推奨)
# allow_origin = ["*"]

# 正規表現を使って特定のオリジンを許可する場合
# import re
# allow_origin = [js.location.origin, re.compile(r"^https?://127\.0\.0\.1(:\d+)?")]


# PostMessageのオリジンが許可されているかどうかを確認する関数
def is_valid_origin(origin, origin_patterns):
    if not isinstance(origin_patterns, list):
        origin_patterns = [origin_patterns]

    for i in range(len(origin_patterns)):
        origin_pattern = origin_patterns[i]
        if isinstance(origin_pattern, str):
            if i == 0 and origin_pattern == "*":
                return True
            if origin == origin_pattern:
                return True
        elif hasattr(origin_pattern, "match"):
            if origin_pattern.match(origin):
                return True

    return False


# Dashから送られたPostMessageを受信して処理するサンプル
def receive_data(event):
    global data

    # オリジンのチェック
    if not is_valid_origin(event.origin, allow_origin):
        js.console.warn("Origin mismatch:", event.origin)
        return

    # 受信したデータをJSONとしてパース
    receive_data = json.loads(event.data)

    # pys_messengerでは常にtypeに"pys_message"という文字列が設定されているはずなので確認する
    if "type" not in receive_data or receive_data["type"] != "pys_message":
        type_str = receive_data["type"] if "type" in receive_data else "unknown"
        js.console.warn("Invalid message type:", type_str)
        return

    # 受信したデータを保存し、コンソールとページ画面に表示
    data = receive_data["data"][0]
    js.console.log("Data received:", event)
    display(f"Receive: {data}")


# PostMessageの受信イベントを登録
js.addEventListener("message", receive_data)


# PostMessageでDashにデータを送信するサンプル
def send_data(event):
    global data
    js.console.log("Data sent:", data + 5)
    # 受信したデータに5を加算してDashに送信
    data += 5
    send_data = {
        "type": "pys_message",        # pys_messengerでは常にこのtypeを設定する必要がある
        "target_id": "iframe_data",   # 送信した値を格納するDash側StoreコンポーネントのIDを設定
        "data": data,                 # 送信するデータを設定
    }
    # PostMessageでDashにデータを送信
    js.parent.postMessage(js.JSON.stringify(send_data), "*")


# クリックで更新した値をDashに送信するためのボタンを作成
button = js.document.createElement("button", id="testButton")
button.textContent = "add5"
js.document.body.appendChild(button)
button.addEventListener("click", send_data)
