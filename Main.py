from GenPDF import PDFGenerator
from RedditConnector import RedditConnection
import sys
import ConfigParser, os

# You dont need to edit any code here. Just run the program to generated the required config and set your user info

if __name__ == '__main__':
    username = ''
    password = ''
    subToCrawl = ''
    client_secret = ''
    client_id = ''

    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.cfg'))
        config.read("config.cfg")
        username = config.get('UserInfo', 'username')
        password = config.get('UserInfo', 'password')

        # client_id = config.get('DeveloperInfo', 'client_id')
        # client_secret = config.get('DeveloperInfo', 'client_secret')

        subToCrawl = config.get('sub', 'subToCrawl')
    except Exception, e:
        print "No config file found\nNot to worry; I made one for you. Please fill in the required info and rerun this program"
        config = ConfigParser.RawConfigParser()

        # config.add_section('DeveloperInfo')
        # config.set('DeveloperInfo', 'client_id', 'YOURID')
        # config.set('DeveloperInfo', 'client_secret', 'YOURSecret')

        config.add_section('UserInfo')
        config.set('UserInfo', 'username', 'YOURUSERNAME')
        config.set('UserInfo', 'password', 'YOURPASSWORD')
        config.add_section('sub')
        config.set('sub', 'subToCrawl', 'programming')
        with open('config.cfg', 'wb') as configfile:
            config.write(configfile)
        exit(1)
   
    p = PDFGenerator()
    tag = "/u/"+username
    redirect_uri = "http://jabbari.me/"
    r = RedditConnection(tag, client_id, client_secret, redirect_uri, username, password)
    p = PDFGenerator()
    p.generateIterator(r.getNPostsFromSub(subToCrawl))