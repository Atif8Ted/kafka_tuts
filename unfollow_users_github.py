import os
import requests
import dotenv
import github

dotenv.load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}
# get list of followers using pygithub
g = github.Github(token)
followers = g.get_user().get_followers()
followers = [follower.login for follower in followers]
# get list of following using pygithub
following = g.get_user().get_following()
following = [follow.login for follow in following]
# get list of users not following me
users_not_following_me = [user for user in following if user not in followers]
# unfollow users not following me


for user in users_not_following_me:
    print(user)
    response = requests.delete(
        f"https://api.github.com/user/following/{user}", headers=headers
    )
    print(response.text)
