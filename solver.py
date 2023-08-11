import requests, json

url = "https://www.letsrevolutionizetesting.com/challenge"

while True:
    payload = {}
    headers = {
    'authority': 'www.letsrevolutionizetesting.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en;q=0.6',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    print(response_json)
    if ("message" not in response_json) or ("message" in response_json and response_json["message"] != "This is not the end"):
        break
    url = response_json["follow"]

