import urllib.error
import urllib.request

try:
    #site = urllib.request.urlopen("https://mangaschan.net/")
    site = urllib.request.urlopen("https://youtube.com/")
except urllib.error.URLError:
    print("Deu ruim")
else:
    print("Deu bom")
    print(site.read())
