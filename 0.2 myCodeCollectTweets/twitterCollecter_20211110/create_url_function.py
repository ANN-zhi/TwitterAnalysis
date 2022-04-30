#Create URL
#access the API to build the request for the endpoint we are going to use and the parameters we want to pass.
def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)
#the search_url I chose here is full-archive search endpoint
#search "Updated endpoints" hereto explore more: https://developer.twitter.com/en/docs/twitter-api/early-access

#find "Query parameters" for [GET /2/tweets/search/all]:
#https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all
#https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all