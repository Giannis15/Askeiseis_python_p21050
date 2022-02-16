from urllib.request import Request, urlopen
import json
import math
from collections import Counter


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
#Metatrepoume ton typo tis data apo byte se dictionary
data= json.loads(data)
b=data['round']

c=b-20
strings=[]
list1=[]

for i in range (c,b):
    #Pairnoume to key randomness apo kathe enan apo tous teleutaious 20 girous
    req = Request('https://drand.cloudflare.com/public/'+str(i), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data= json.loads(data)
    
    strings.append(data['randomness'])

#Enwnoume ta 16dika strings poy vrikame prin ,wste na ypologisoume stin synexeia tin entropy
x="".join(strings)


#Xrisimopoioume tin function entropy ,wste na ypologisoume tin entropia tou string x
def entropy(x):
    p, lns = Counter(x), float(len(x))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())
print(entropy(x))