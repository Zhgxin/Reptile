# -*- coding:utf-8 -*-
import urllib2


class HtmlDownloader(object):
    #下载
    def download(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            print response

        return response.read()
