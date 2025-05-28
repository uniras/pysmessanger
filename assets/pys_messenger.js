// Settings
allow_message_origin = [globalThis.location.origin];

// Receiver from PyScript
globalThis.addEventListener("message", function (event) {
    let valid_origin = false;
    for (let i = 0; i < allow_message_origin.length; i++) {
        if (RegExp(allow_message_origin[i]).test(event.origin)) {
            valid_origin = true;
            break;
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
globalThis.dash_clientside = globalThis.dash_clientside || {};
globalThis.dash_clientside.pys_sender = globalThis.dash_clientside.pys_sender || {};

globalThis.dash_clientside.pys_sender.pys_send = function (target_frame_id, ...args) {
    const target_frame = document.getElementById(target_frame_id);
    if (!target_frame || !target_frame.contentWindow) {
        console.error("Invalid target frame provided:", target_frame);
        return;
    }

    const target_frame_origin = target_frame.contentWindow.location.origin;

    try {
        const message = {
            type: "pys_message",
            target_id: target_frame_id,
            data: args
        }
        const formattedMessage = JSON.stringify(message);
        target_frame.contentWindow.postMessage(formattedMessage, target_frame_origin);
    } catch (error) {
        console.error("Failed to send message:", error);
    }

    return "";
}