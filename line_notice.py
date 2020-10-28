import requests
import dotenv_loader


# Lineにメッセージを送信する関数　送信したい文字列を引数に定義
def send(send_message):
    line_notify_token = dotenv_loader.token
    line_notify_api = 'https://notify-api.line.me/api/notify'

    # トークン情報をヘッダーに載せる
    headers = {'Authorization': f'Bearer {line_notify_token}'}

    data = {'message': send_message}
    # 送信
    requests.post(line_notify_api, headers = headers, data = data)


if __name__ == "__main__":
    text = "test"
    send(text)