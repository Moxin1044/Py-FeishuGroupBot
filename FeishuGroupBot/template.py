import requests
import json

def send_feishu_card_message(webhook_url, title, message):
    """
    发送卡片消息到飞书机器人 webhook。

    :param webhook_url: 飞书机器人的 webhook 地址
    :param title: 发送的标题
    :param message: 要发送的消息
    :return: 响应对象
    """
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "msg_type": "interactive",
        "card": {
            "schema": "2.0",
            "config": {
                "update_multi": True,
                "style": {
                    "text_size": {
                        "normal_v2": {
                            "default": "normal",
                            "pc": "normal",
                            "mobile": "heading"
                        }
                    }
                }
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": title
                },
                "subtitle": {
                    "tag": "plain_text",
                    "content": ""
                },
                "template": "blue",
                "padding": "12px 12px 12px 12px"
            },
            "body": {
                "direction": "vertical",
                "padding": "12px 12px 12px 12px",
                "elements": [
                    {
                        "tag": "markdown",
                        "content": message,
                        "text_align": "left",
                        "text_size": "normal_v2",
                        "margin": "0px 0px 0px 0px"
                    }
                ]
            }
        }
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    return response


def send_feishu_text_message(webhook_url, message):
    """
    发送文本消息到飞书机器人 webhook。

    :param webhook_url: 飞书机器人的 webhook 地址
    :param message: 要发送的文本消息
    :return: 响应对象
    """
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    return response

