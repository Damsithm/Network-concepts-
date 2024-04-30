#!/usr/bin/env python3
import tweepy

# Reference the API v2 Tweepy Documentation here:
# https://docs.tweepy.org/en/stable/index.html

# ====== #

###################################################################
# IMPORTANT: MAKE SURE TO DELETE TOKENS BEFORE UPLODING TO GITHUB #
#            IF YOU PLAN TO SAVE YOUR WORK ONLINE                 #
###################################################################

# Enter Authentication information here:
# NOTE: Consumer Key/Secret is another name for API Key/Secret
client = tweepy.Client(bearer_token='enter-token', 
                   consumer_key='enter-consumer-key', 
                   consumer_secret='enter-consumer-secret', 
                   access_token='enter-access-token', 
                   access_token_secret='enter-secret')

try:
    me = client.get_me()

    # If authentication worked, you should get your @ name returned here
    print(f"Your Name Is: {me[0]['name']}")
    print("Authentication OK")
    print("\n====\n")
    
except:
    print("Error during authentication")
    
    #Uncomment the below line for detailed error information
    # raise

# ====== #

# Tweet With the API
'''ENTER YOUR CODE HERE'''

# ====== #

# Read Tweets with the API
'''ENTER YOUR CODE HERE'''
