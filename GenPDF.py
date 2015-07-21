import os
import pdfkit
from readability.readability import Document
import urllib
from urlparse import urlparse
import tldextract

class PDFGenerator(object):
    """docstring for PDFGenerator"""
    def __init__(self, path="pdf"):
        super(PDFGenerator, self).__init__()
        self.path=path
        self.options = {
    'page-size': 'Letter',
    'minimum-font-size': '18',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'quiet': ''
    }
        if not os.path.exists(path):
            os.makedirs(path)

    def generatePDF(self, url):
        ext = tldextract.extract(url)
        domain=  ext.domain+"."+ext.tld
        html = urllib.urlopen(url).read()
        readable_article = Document(html).summary()
        readable_title = Document(html).short_title()
        self.options["title"] = readable_title

        pdfkit.from_string(readable_article, self.path+"/"+domain+"-"+readable_title+'.pdf', options=self.options)

    def generateIterator(self, item):
        for i in item:
            if "reddit.com" not in i.url:
                print i
                try:
                    self.generatePDF(i.url)
                except Exception, e:
                    with open("log.log", "a+") as f:
                        f.write("================")
                        f.write(i.url)
                        f.write(str(e))
                        f.write("================")


if __name__ == '__main__':
    p = PDFGenerator()
    p.generatePDF("http://joubin.me")
   