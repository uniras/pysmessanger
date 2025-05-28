import js  # type: ignore
import json
from pyscript import display  # type: ignore

data = json.loads(js.decodeURIComponent(js.location.search).split("&")[0].split("=")[1])

display(f"Receive: {data["value"]}")
