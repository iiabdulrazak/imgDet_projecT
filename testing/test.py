from stable import *

#testing if we can get the tweet link out of the results
sample_result = all_results[1]
tweet_id = sample_result.id_str
screen_name = sample_result.user.screen_name

tweet_url = "https://twitter.com/{screen_name}/status/{tweet_id}"
tweet_url = tweet_url.format(screen_name=screen_name,tweet_id=tweet_id)

print(f"Tweet Link: {tweet_url}")
