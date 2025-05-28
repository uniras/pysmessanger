globalThis.dash_clientside = globalThis.dash_clientside || {};
globalThis.dash_clientside.pys_sender = globalThis.dash_clientside.pys_sender || {};

globalThis.dash_clientside.pys_sender.pys_send = function (target_frame_id, ...args) {
    const target_frame = document.getElementById(target_frame_id);
    if (!target_frame || !target_frame.contentWindow) {
        console.error("Invalid target frame provided:", target_frame);
        return;
    }

    try {
        const message = JSON.stringify(args);
        target_frame.contentWindow.postMessage(message, "*");
    } catch (error) {
        console.error("Failed to send message:", error);
    }

    return "";
}