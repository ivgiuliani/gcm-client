#!/usr/bin/env python

"""
Simple Google Cloud Messaging client.
"""

import sys
import json
import select
import requests


GCM_SERVER = "https://gcm-http.googleapis.com/gcm/send"


def is_api_key_valid(api_key):
    payload = {
        "registration_ids": ["not_important"]
    }
    request = requests.post(
        GCM_SERVER,
        headers=build_headers(api_key),
        data=payload
    )

    return request.status_code != 401


def build_headers(api_key):
    return {
        "Authorization": "key=" + api_key,
        "Content-Type": "application/json",
    }


def send(api_key, to, data, collapse_key=None, ttl=None, delay_while_idle=None):
    base_payload = {
        "to": to,
    }

    payload = data.copy()
    payload.update(base_payload)

    if collapse_key:
        payload.update({"collapse_key": collapse_key})

    if ttl:
        payload.update({"time_to_live": ttl})

    if delay_while_idle is not None:
        payload.update({"delay_while_idle": delay_while_idle})

    request = requests.post(
        GCM_SERVER,
        headers=build_headers(api_key),
        data=payload
    )

    if request.status_code != 200:
        raise Exception(
            "invalid request: " + request.text.strip() + " (status code = " + str(request.status_code) + ")"
        )

    return request.json()


def main(args):
    api_key, to = args[1], args[2]

    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        # Read data from stdin if available
        data = sys.stdin.read()
    else:
        data = args[3]

    if not is_api_key_valid(api_key):
        print("Supplied API key is not valid.")
        return True

    print("API key is valid: " + str(is_api_key_valid(api_key)))
    print("---------------------------------------------------")

    input_object = json.loads(data)

    print("Response:")
    response = send(api_key, to, input_object)
    print(json.dumps(response, indent=4))

    return False


if __name__ == "__main__":
    sys.exit(main(sys.argv))
