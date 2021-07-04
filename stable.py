#importing needed packages and checking if their is an issues!
try:
	import os
	import twitter
	import config as cf
	import urllib.request
except Exception as e:
	print(f"Issue While Importing Packages!\n{e}")

#declaring credentials on config.py file!
api = twitter.Api(consumer_key = cf.credentials["consumer_key"],
                  consumer_secret = cf.credentials["consumer_secret"],
                  access_token_key = cf.credentials["access_token"],
                  access_token_secret = cf.credentials["access_token_secret"])

#now we configure the hashtags and other settings to retrieve
hashtag = 'ضحك' #hashtag
result_type = 'mixed' #possible values: mixed, recent, popular
include_entities = 'true'
with_twitter_user_id = 'true' #include user information
since = '2021-04-29' #start date
until = '2021-05-01' #end date
count = '50' #number of tweets to return per page

#initializing the query and test it
query = ('q={hashtag}' + 
         '&result_type={result_type}' +
         '&include_entities={include_entities}' +
         '&with_twitter_user_id={with_twitter_user_id}' + 
         '&since={since}' + 
         '&until={until}' +
         '&count={count}')

query = query.format(hashtag=hashtag,
                 result_type=result_type,
                 include_entities=include_entities,
                 with_twitter_user_id=with_twitter_user_id,
                 since=since,
                 until=until,
                 count=count)
#testing if the query works!
# print(f"Query Structure: \n\n({query})")

#lets now check the id of the tweet
all_results = []
max_id = None
IDs = []

for i in range(0,300):
    
    results = api.GetSearch(raw_query = query)
    all_results.extend(results)
    IDs = [result.id for result in results]
    smallest_ID = min(IDs)
    
    if max_id == None: # first call 
        max_id = smallest_ID
        query += '&max_id={max_id}'.format(max_id=max_id)
    else:
        old_max_id = "max_id={max_id}".format(max_id=max_id)
        max_id = smallest_ID
        new_max_id = "max_id={max_id}".format(max_id=max_id)
        query = query.replace(old_max_id,new_max_id)

#checking if we are getting ids back from the api
# and the length of all_results
print(f"last max_id = {max_id}")
print(f"length all_results = {len(all_results)}")

#now lets see the output from the data we get from the API
print(f"First Result:\n\n{all_results[0]}")
#and let us see the first person details
print(f"ID: {all_results[0].id_str}, Name: {all_results[0].user.screen_name}")
