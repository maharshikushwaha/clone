import requests 
import bs4
import time
ind = [ "Saving", "Please Wait", "This script is written By Maharshi Kushwaha", "Python is lob"]

url=input("Please Enter Your Target Page URL: \t")
fName=input("Enter Filename:\t ")
fName=fName + ".html"
response=requests.get(url)
bs = bs4.BeautifulSoup(response.text, "html.parser")
data=bs.prettify()
with open(fName, "w+") as f:
	f.write(data)
	

for m in ind:
  	print(f"{m}" + " " * 9, end='\r')
  	time.sleep(0.5)


final = "Your File :" + fName + " has been saved" + "Thanks"
print(final + "This script is written By Maharshi Kushwaha")
