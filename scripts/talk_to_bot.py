import requests
import time


def send_msg(msg):
    url = 'http://localhost:5005/webhooks/rest/webhook'
    headers = {"Content-type": "application/json"}
    data = {"sender": "script", "message": msg}
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    msg_list = [
        "Coucou",
        'je vais couler une douille',
        "combien j'ai fumé aujourd'hui ?"
    ]

    for msg in msg_list:
        print(send_msg(msg))
        time.sleep(1.5)
