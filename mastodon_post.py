from mastodon import Mastodon

accessToken = input("Enter Mastodon access token : ")
api_base_url = input("Enter Mastodon URL (just press enter to use 'https://mastodon.social'): ")
postText = input("Write what you want to post: ")
if (api_base_url == "") :
    apiBaseUrl = 'https://mastodon.social'

mClient = Mastodon(
    access_token = accessToken.strip(), #remove trailing and leading whitespaces from input
    api_base_url = apiBaseUrl)

try:
    mClient.status_post(postText)
    print("Successfully posted")
except Exception as e:
    print("Error", e)