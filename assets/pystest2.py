import js  # type: ignore
import json
from pyscript import display  # type: ignore

data = 50


def send_data(event):
    global data
    js.console.log("Data sent:", data + 5)
    data += 5
    send_data = {
        "type": "pys_message",
        "target_id": "iframe_data",
        "data": data,
    }
    js.parent.postMessage(js.JSON.stringify(send_data), "*")


def receive_data(event):
    global data
    if event.origin != js.location.origin:
        js.console.warn("Origin mismatch:", event.origin)
        return
    receive_data = json.loads(event.data)
    if "type" not in receive_data or receive_data["type"] != "pys_message":
        type_str = receive_data["type"] if "type" in receive_data else "unknown"
        js.console.warn("Invalid message type:", type_str)
        return
    js.console.log("Data received:", event)
    data = receive_data["data"][0]
    display(f"Receive: {data}")


js.addEventListener("message", receive_data)

button = js.document.createElement("button", id="testButton")
button.textContent = "add5"
js.document.body.appendChild(button)
button.addEventListener("click", send_data)
