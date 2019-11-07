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
        url=('https://newsapi.org/v2/top-headlines?''country=in&''apiKey=2c653aaad7e74b73ad5160b2be0cbbde')
    else:
        country=request.POST['country']
        category=request.POST['category']
        if type(country)!=type("none") or type(category) != type("none") :
            url=('https://newsapi.org/v2/top-headlines?''country=in&''apiKey=2c653aaad7e74b73ad5160b2be0cbbde')
        else:    
            url='https://newsapi.org/v2/top-headlines?'+'country='+country+'&'+'category='+category+'&'+'apiKey=2c653aaad7e74b73ad5160b2be0cbbde'

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

# def articles(request,articlenumber):
#     return render(request,'Home/Article.html',{'article':discript[articlenumber],'links':urls[articlenumber],'imglinks':imageurls[articlenumber]})

# /*def filter(request):
#     if request.method=='POST':
#         country=request.POST['country']
#         category=request.POST['category']
#         head=[]
#         discript=[]
#         urls=[]
#         imageurls=[]
        
#         url='https://newsapi.org/v2/top-headlines?'+'country='+country+'&'+'category='+category+'&'+'apiKey=2c653aaad7e74b73ad5160b2be0cbbde'
#         response=requests.get(url)
#         return render(request,'Home/index.html',{'headings':head,'articles':discript,'imglinks':imageurls,'urls':urls})

# */