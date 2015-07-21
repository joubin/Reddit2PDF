import praw
import imghdr, urllib, cStringIO
import uuid
import urllib2
import os, sys
from imgurpython import ImgurClient
from subprocess import call
import time

class RedditConnection(object):
    """provides a connection to reddit"""
    def __init__(self, client_tag,client_id, client_secret, redirect_uri, username, password):
        super(RedditConnection, self).__init__()
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.username = username
        self.connection = self.authenticate(client_secret, password, client_tag)

    def authenticate(self, client_secret, password, client_tag):
        r = praw.Reddit(client_tag)
        r.set_oauth_app_info(client_id=self.client_id,
                 client_secret=client_secret,
                 redirect_uri=self.redirect_uri
                              )
        r.login(self.username, password)
        return r

    def getNPostsFromSub(self, sub_reddit, limit=None):
        return self.connection.get_subreddit(sub_reddit).get_hot(limit=limit)


    def getLinkFromSub(self, sub):
        return sub.url

    def toString(self, items):
        if type(items) == str:
            print items
        else:
            for i in items:
                print i

try:
    pass
except Exception, e:
    raise e