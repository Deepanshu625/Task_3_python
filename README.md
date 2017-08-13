# Task_3_python
first_version

 In order to access Twitter Streaming API, we need to get 4 pieces of information from Twitter: API key, API secret, Access token and Access token secret.

    step 1:
    		application name:		Tweeter_handler
    		api key			:		2ngBLnu5eBPJSOQkALxFRjJlt
    		api secret		:		hFLFFJPbTah29QuH3EUvtBh9BGl4efAZeqxlIHuFyBOLyeSQqJ
    		access token link:		571498789-XcLNRHyW6UwnAH0WYUEsNXDhhAYSzXV8ZfVg2Xkg
    		access token secret:	CBTpmSRVUWOUqT3r8dWYVgyLFfPtnvOnDm4HK2xdZ4Bga

    step 2:
    		We will be using a Python library called Tweepy to connect to Twitter Streaming API and downloading the data. 


    step 3:
    		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth)

    		getting error while running		ImportError: No module named tweepy

    		soleved by stackoverflow:https://stackoverflow.com/questions/27451316/importerror-no-module-named-tweepy
    		Don't use sudo to call pip when you're in a virtualenv: the root user won't have the virtualenv activated so the package is installed globally, as you can see from the paths. Just run pip install tweepy.

    step 4:
    		We can capture this data into a file that we will use later for the analysis by following command: 
    		python twitter_streaming.py > twitter_data.txt.
    
    step 5:
    		#To get list of all followers:

			for user in tweepy.Cursor(api.followers, screen_name="deepanshu sharma").items():
    			print user.screen_name
    step 6:
    		#To get the list of all following users

			for user in tweepy.Cursor(api.friends, screen_name="deepanshu sharma").items():
    			print user.screen_name
