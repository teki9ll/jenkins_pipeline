import requests
import sys
import json
import argparse

def post_to_endpoint(url, json_data):
    try:
        response = requests.post(url, json=json_data)
        response.raise_for_status()
        response_data = response.json()
        if response_data.get('status') == 'FAIL':
            print("Status is FAIL, exiting with code -1")
            sys.exit(-1)
        else:
            print("Request successful. Response data:", response_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(-1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        sys.exit(-1)

def main():
    parser = argparse.ArgumentParser(description='Send a JSON POST request to a specified URL.')
    parser.add_argument('url', type=str, help='The URL to post the JSON data to.')
    parser.add_argument('json_data', type=str, help='The JSON data to send in the POST request.')

    args = parser.parse_args()

    try:
        json_data = json.loads(args.json_data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
        sys.exit(-1)

    post_to_endpoint(args.url, json_data)

if __name__ == "__main__":
    main()
