import json
import requests


def task_publish(task, base_url, user, pwd, eui):
    """
    任务下发
    """
    url = f"{base_url}device/task_publish"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"eui": eui, "taskSetting": task})
    # print("DEBUG[task_publish]", data)
    response = requests.post(url, headers=headers, data=data, auth=(user, pwd))
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def llm_chat(words, base_url, user, pwd, eui):
    """
    任务拆解
    """
    url = f"{base_url}device/llm_chat"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"input": words, "eui": eui})
    # print("DEBUG[llm_chat]", data)
    response = requests.post(url, headers=headers, data=data, auth=(user, pwd))
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
