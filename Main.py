from GenPDF import PDFGenerator
from RedditConnector import RedditConnection
import sys

if __name__ == '__main__':
    # p = PDFGenerator()
    # # p.generatePDF("http://joubin.me")
    tag = "/u/ichillax"
    client_id = '6DJslTypr_Gw4g'
    client_secret='F54H-YIBreoGUZav2kyLyWAeZPo'
    username = "ichillax"
    password = "YOURPASSWORD"
    redirect_uri = "http://joubin.me/"
    r = RedditConnection(tag, client_id, client_secret, redirect_uri, username, password)
    p = PDFGenerator()
    p.generateIterator(r.getNPostsFromSub("netsec"))

