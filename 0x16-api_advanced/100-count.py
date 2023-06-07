#!/usr/bin/python3
"""Find the number of subs"""
import requests
import shlex

def print_words(word_list=[], hot_list=[]):
    print(word_list)
    print(len(hot_list))
    for word in word_list:
        count = 0
        print(word)
        for title in top_post:
            if word in shlex.split(title):
                count += 1
        print("{}: {}".format(word, count))



def count_words(subreddit, word_list=[], hot_list=[], after=""):
    """ show the top 10 posts in a subreddit """
    try:
        # Change the user agent
        headers = {'User-Agent': 'cmmolanos'}
        payload = {'t': 'all', 'after': after}
        request = requests.get('https://api.reddit.com/r/{}/hot'.
                               format(subreddit), headers=headers,
                               params=payload)
        top_posts = request.json()

        for post in top_posts['data']['children']:
            hot_list.append(post['data']['title'])

        after = top_posts['data']['after']
        print(word_list)
        print(after)
        if after is not None:
            count_words(subreddit, word_list, hot_list, after)

        return (print_words(word_list, hot_list))

    except:
        return None
