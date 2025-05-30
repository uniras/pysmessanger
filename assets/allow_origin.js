// pys_messenger内で使うPostMessageのオリジンに関する設定サンプル

// エラーを抑制するためグローバル変数の存在確認と定義
globalThis.dash_clientside = globalThis.dash_clientside || {};
globalThis.dash_clientside.pys_receiver = globalThis.dash_clientside.pys_receiver || {};
globalThis.dash_clientside.pys_sender = globalThis.dash_clientside.pys_sender || {};


// 受信を許可するオリジンをリストで設定するサンプル、文字列または正規表現の配列で設定する
// すべてのオリジンを認める場合は配列の最初の要素を文字列の*にする(非推奨)
// デフォルトでは同一オリジンのみを許可、正規表現リテラルで指定して正規表現でマッチさせることも可能
//globalThis.dash_clientside.pys_receiver.allow_message_origin = [globalThis.location.origin, /https?:\/\/localhost(:\d+)?/];


// 送信時に使うオリジン設定のサンプル、デフォルトでは*を使用
//globalThis.dash_clientside.pys_sender.send_origin = "http://127.0.0.1:8050";
