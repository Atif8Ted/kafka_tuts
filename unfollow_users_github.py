import os
import requests
import dotenv

dotenv.load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}
# get list of users following me
response = requests.get("https://api.github.com/user/followers", headers=headers)
followers = response.json()
followers = [follower["login"] for follower in followers]
# get list of users I am following
response = requests.get("https://api.github.com/user/following", headers=headers)
following = response.json()
print(following)
following = [follow["login"] for follow in following]
# get list of users I am following that are not following me
users_not_following_me = [user for user in following if user not in followers]
print(users_not_following_me)
# unfollow users
for user in users_not_following_me:
    response = requests.delete(
        f"https://api.github.com/user/following/{user}", headers=headers
    )
    print(response.text)
