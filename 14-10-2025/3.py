# From a Twitter post, extract both hashtags (#) and mentions (@), and display the count for each.
import re

tweet = "Hey @user1, check this out! #exciting #news @user2"

hashtags = re.findall(r"#(\w+)", tweet)
mentions = re.findall(r"@(\w+)", tweet)

print("Hashtags:", hashtags)
print("Mentions:", mentions)
print("Hashtag count:", len(hashtags))
print("Mention count:", len(mentions))