// pys_messenger内で使うPostMessageのオリジンに関する設定サンプル

// エラーを抑制するためグローバル変数の存在確認と定義
globalThis.dash_clientside = globalThis.dash_clientside || {};
globalThis.dash_clientside.pys_receiver = globalThis.dash_clientside.pys_receiver || {};
globalThis.dash_clientside.pys_sender = globalThis.dash_clientside.pys_sender || {};


// 受信を許可するオリジンをリストで設定するサンプル。デフォルトでは同一オリジンのみを許可。
// 正規表現リテラルで指定して正規表現でマッチさせることも可能
//globalThis.dash_clientside.pys_receiver.allow_message_origin = [globalThis.location.origin, /https?:\/\/localhost(:\d+)?/];


// 送信時に使うオリジン設定のサンプル、デフォルトでは*を使用
//globalThis.dash_clientside.pys_sender.send_origin = "*";

