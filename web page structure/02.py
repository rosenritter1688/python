import urllib ##a module for retrieving a URL
import urllib.request
with urllib.request.urlopen("https://www.yahoo.co.jp/") as respone:
    html = respone.read()