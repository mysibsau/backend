import requests
from config.settings import env
from ..api.serializers import NotificationsSerializer 
from json import loads


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'key={env.str("FIREBASE_TOKEN")}',
}


def send_notification(notification, context):
    result = []
    for json in NotificationsSerializer(notification, context):
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, json=json)
        result.append(
            str(loads(response.text).get('message_id', 0))
        )

    return result
