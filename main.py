import json
import requests

if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "referer": "https://www.bilibili.com",
    }

    baseUrl = "https://api.bilibili.com/x/web-interface/view"
    #url     = baseUrl + "?" + "bvid=BV1k94y1u7bh"
    url     = baseUrl + "?" + "bvid=BV1jm411y7py" # UgcSeason

    response = requests.get(url, headers=headers).text
    res      = json.loads(response)["data"]

    print(type(res))


    from pprint import pprint
    pprint(res)