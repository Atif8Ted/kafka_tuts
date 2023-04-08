# importing all dependencies
import os

import requests
import base64
import dotenv

dotenv.load_dotenv()
# Define your keys from the developer portal
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_SECRET")

ids = {23424848}


def get_twitter_data():
    key_secret = "{}:{}".format(consumer_key, consumer_secret).encode("ascii")
    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    # Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode("ascii")
    base_url = "https://api.twitter.com/"
    auth_url = "{}oauth2/token".format(base_url)
    auth_headers = {
        "Authorization": "Basic {}".format(b64_encoded_key),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    auth_data = {"grant_type": "client_credentials"}
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    print(auth_resp.status_code)
    access_token = auth_resp.json()["access_token"]
    trend_headers = {"Authorization": "Bearer {}".format(access_token)}

    trend_url = "https://api.twitter.com/1.1/trends/place.json"
    for id in ids:
        trend_resp = requests.get(trend_url, headers=trend_headers, params={"id": id})
        tweet_data = trend_resp.json()
        for i in tweet_data:
            for j in range(len(i["trends"])):
                yield i["trends"][j]
