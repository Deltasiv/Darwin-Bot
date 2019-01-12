import urllib3
from bs4 import BeautifulSoup
import requests 
import time 

start = time.time() 

websiteCode = urllib3.urlopen("http://google.com).read() 
soup = BeautifulSoup(websiteCode)   

images = [] 
images = soup.findAll("img")

for image in images: 
    
    print(image.get("src")) 

end = time.time() 

print(end - start) 
