import requests


def main():
    send_line_notify('てすとてすと')


def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'ここに発行したトークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers=headers, data=data)


if __name__ == "__main__":
    main()
