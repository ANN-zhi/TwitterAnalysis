#Create URL
#access the API to build the request for the endpoint we are going to use and the parameters we want to pass.
def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id',
                    'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld',
                    'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld',
                    'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)
#the search_url I chose here is full-archive search endpoint
#search "Updated endpoints" hereto explore more: https://developer.twitter.com/en/docs/twitter-api/early-access

#find "Query parameters" for [GET /2/tweets/search/all]:
#https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all
#https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all