#!/usr/bin/env python3

import json
import requests


def createDate(year, month, day):
    return f'{year}-{month}-{day}'


def add_topic_to_db(dictionary):
    payload = json.dumps(dictionary, ensure_ascii=False)
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/topic", headers={"Content-type": "application/json"}, data=payload)
    if response.status_code != 201:
        raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
    print(response.json())

def add_numeric_entry_to_db(dictionary):
    payload = json.dumps(dictionary, ensure_ascii=False)
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/numericentry", headers={"Content-type": "application/json"}, data=payload)
    if response.status_code != 201:
        raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
    print(response.json())


add_topic_to_db({
    'name': 'Weight tracking',
    'question': None,
    'supportedUnit': 'kg',
    'combinationOperation': 'avg'
})
add_topic_to_db({
    'name': 'Food spending',
    'question': 'What food was purchased?',
    'supportedUnit': 'HUF',
    'combinationOperation': 'sum'
})
add_topic_to_db({
    'name': 'Activity',
    'question': 'What activity was done?',
    'supportedUnit': 'min',
    'combinationOperation': 'sum'
})


topics = requests.get("http://127.0.0.1:8000/api/v1/topic")


weight_topic = [t for t in topics.json() if t['name'] == 'Weight tracking'][0]
food_spending_topic = [
    t for t in topics.json() if t['name'] == 'Food spending'][0]
activity_topic = [t for t in topics.json() if t['name'] == 'Activity'][0]


add_numeric_entry_to_db({
    'topic_id': weight_topic['id'],
    'answer': None,
    'value': 86,
    'date': createDate(year=2022, month=12, day=10)
})

add_numeric_entry_to_db({
    'topic_id': weight_topic['id'],
    'answer': None,
    'value': 85,
    'date': createDate(year=2022, month=12, day=11)
})

add_numeric_entry_to_db({
    'topic_id': weight_topic['id'],
    'answer': None,
    'value': 85.2,
    'date': createDate(year=2022, month=12, day=12)
})


add_numeric_entry_to_db({
    'topic_id': food_spending_topic['id'],
    'answer': 'Kefir',
    'value': 425,
    'date': createDate(year=2022, month=12, day=12)
})

add_numeric_entry_to_db({
    'topic_id': food_spending_topic['id'],
    'answer': 'Bananas 1kg',
    'value': 700,
    'date': createDate(year=2022, month=12, day=12)
})

add_numeric_entry_to_db({
    'topic_id': food_spending_topic['id'],
    'answer': 'Bananas 1,5kg',
    'value': 1000,
    'date': createDate(year=2022, month=12, day=14)
})


add_numeric_entry_to_db({
    'topic_id': activity_topic['id'],
    'answer': 'Cycling',
    'value': 15,
    'date': createDate(year=2022, month=12, day=11)
})

add_numeric_entry_to_db({
    'topic_id': activity_topic['id'],
    'answer': 'Running',
    'value': 20,
    'date': createDate(year=2022, month=12, day=13)
})

add_numeric_entry_to_db({
    'topic_id': activity_topic['id'],
    'answer': 'Workout',
    'value': 90,
    'date': createDate(year=2022, month=12, day=14)
})

add_numeric_entry_to_db({
    'topic_id': activity_topic['id'],
    'answer': 'Running',
    'value': 30,
    'date': createDate(year=2022, month=12, day=14)
})
