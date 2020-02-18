from django.shortcuts import render
from .models import scrapped
import requests
from bs4 import BeautifulSoup
import io
# Create your views here.
def index(request):
	return render(request, 'index.html',{'name':'azhar'})

def outcome(request):
	filename="product.csv"
	f=open(filename,"w")
	a=[]
	b=[]
	k=0
	city=request.GET["city"]
	sale=request.GET["sale"]
	pagesCount=request.GET["pagesCount"]
	pagesCount=int(pagesCount)+1
	headers ={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
	for j in range(1,int(pagesCount)):
		URL1='https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=ahmedabad'
		URL ='https://www.magicbricks.com/property-for-'+str(sale)+'/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName='+str(city)+'&mbTrackSrc=tabChange&page='+str(j)+'&category=S'
		#URL ='https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=ahmedabad&mbTrackSrc=tabChange&page=1&category=S'
		page = requests.get(URL, headers=headers)
		soup = BeautifulSoup(page.text,'lxml')
		for i in soup.select('span[class*="m-srp-card__title"]'):
			if(k%2==0):
				temp=i.get_text()
				temp=temp.replace("\n"," ")
				temp=temp.replace("  ","")
				temp=temp.replace("\t","")
				temp=temp.replace(","," ")
				a.append(temp)
			k=k+1
		for i in soup.select('div[class*="m-srp-card__price"]'):
			temp=i.get_text()
			b.append(temp[2:])

	temper=""
	for i in range(0,len(b)):
		temper=temper+"Rs "+b[i]+","+a[i]+"\n"
		f.write("Rs "+b[i]+",\t"+a[i]+"\n")
	
	return render(request, 'result.html',{'rest':temper})