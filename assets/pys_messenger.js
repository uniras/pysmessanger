globalThis.dash_clientside = globalThis.dash_clientside || {};

// Receiver from PyScript
globalThis.dash_clientside.pys_receiver = globalThis.dash_clientside.pys_receiver || {};
globalThis.dash_clientside.pys_receiver.allow_message_origin_default = [globalThis.location.origin];

globalThis.addEventListener("message", function (event) {
    let valid_origin = false;
    let allow_message_origin = globalThis.dash_clientside.pys_receiver.allow_message_origin || globalThis.dash_clientside.pys_receiver.allow_message_origin_default;

    if (!Array.isArray(allow_message_origin)) allow_message_origin = [allow_message_origin];

    for (let i = 0; i < allow_message_origin.length; i++) {
        if (i == 0 && allow_message_origin[i] === "*") {
            valid_origin = true;
            break;
        } else if (allow_message_origin[i] instanceof RegExp) {
            if (allow_message_origin[i].test(event.origin)) {
                valid_origin = true;
                break;
            }
        } else if (typeof allow_message_origin[i] === "string") {
            if (event.origin === allow_message_origin[i]) {
                valid_origin = true;
                break;
            }
        }
    }

    if (!valid_origin) {
        console.warn("Received message from invalid origin:", event.origin);
        return;
    }

    if (event.data) {
        parsedata = JSON.parse(event.data);
        if (typeof parsedata.type !== "string" || parsedata.type !== "pys_message") return;
        if (!parsedata || !parsedata.target_id || !parsedata.data) {
            console.error("Invalid data received:", parsedata);
            return;
        }
        dash_clientside.set_props(parsedata.target_id, parsedata);
    }
});

// Sender to PyScript
globalThis.dash_clientside.pys_sender = globalThis.dash_clientside.pys_sender || {};
globalThis.dash_clientside.pys_sender.send_origin_default = "*"

globalThis.dash_clientside.pys_sender.pys_send = function (target_frame_id, ...args) {
    const target_frame = document.getElementById(target_frame_id);
    if (!target_frame || !target_frame.contentWindow) {
        console.error("Invalid target frame provided:", target_frame);
        return;
    }

    const send_origin = globalThis.dash_clientside.pys_sender.send_origin || globalThis.dash_clientside.pys_sender.send_origin_default;

    try {
        const message = {
            type: "pys_message",
            target_id: target_frame_id,
            data: args
        }
        const formattedMessage = JSON.stringify(message);
        target_frame.contentWindow.postMessage(formattedMessage, send_origin);
    } catch (error) {
        console.error("Failed to send message:", error);
    }

    return "";
}
