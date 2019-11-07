from django.shortcuts import render
import requests
head=[]
discript=[]
urls=[]
imageurls=[]
# Create your views here.
def index(request):
    url=""
    if request.method=='GET':
        url=('https://newsapi.org/v2/top-headlines?''country=in&''apiKey=API_KEY')
    else:
        country=request.POST['country']
        category=request.POST['category']
        if type(country)!=type("none") or type(category) != type("none") :
            url=('https://newsapi.org/v2/top-headlines?''country=in&''apiKey=API_KEY')
        else:    
            url='https://newsapi.org/v2/top-headlines?'+'country='+country+'&'+'category='+category+'&'+'apiKey=API_KEY'

    response=requests.get(url)
    Articles=response.json()['articles'];  
    head=[]
    discript=[]
    urls=[]
    imageurls=[]
    for sp in Articles:
            urls.append(str(sp['url']))
            imageurls.append(str(sp['urlToImage']))
            head.append(sp['title'])
            discript.append(sp['description'])
    return render(request,'Home/index.html',{'headings':head,'articles':discript,'imglinks':imageurls,'urls':urls})

