from bs4 import beautifulSoup 
from urllib.request import Request, urlopen
url = 'http://api.ipstack.com/156.209.145.228?access_key=2390f189d22408b2db29e7524d305658'
rep = request(url, headers={'User-agent':'Mozilla/5.0'})
a = urlopen(req)
b = a.read()
soup = BeautifulSoup(b.decode(),'html.parser')
t = str(soup)
c = t.strip(',')
ss = list(c)
for i in c.split(','):
    x = i.strip('\\')
    r = x.strip('''')
    io = r.replace("",")
    fo = io.replace('}',")
    mo = fo.replace('{',")
    zo = mo.replace(']',")
    vv = zo.replace('/',")
    vvv = vv.replace('[',")
    print('='*50)
    print(vvv+'  ')
    print('='*50)
              
