allow_origin = window.location.origin;

globalThis.addEventListener("message", function (event) {
    if (event.origin !== allow_origin) {
        console.warn("Received message from unauthorized origin:", event.origin);
        return;
    }

    if (event.data) {
        parsedata = JSON.parse(event.data);
        if (!parsedata || !parsedata.target_id || !parsedata.data) {
            console.error("Invalid data received:", parsedata);
            return;
        }
        dash_clientside.set_props(parsedata.target_id, parsedata);
    }
});