import requests
import argparse
import json
import sys

def send_post_req(url, data):
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        response_data = json.loads(response.text)
        if response_data.get("status") == "FAIL":
            print(response_data.get("status"))
            sys.exit(-1)
        else:
            print(response_data.get("status"))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(-1)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        sys.exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a POST request to a URL with dictionary data")
    parser.add_argument("url", type=str, help="URL to send the POST request to")
    parser.add_argument("json_data", type=str, help="Dictionary data to send with the POST request")

    args = parser.parse_args()
    json_data = args.json_data.replace("'", "\"")
    try:
        send_post_req(args.url, json.loads(json_data))
    except ValueError as e:
        print("Invalid JSON data provided:", e)
        sys.exit(-1)
