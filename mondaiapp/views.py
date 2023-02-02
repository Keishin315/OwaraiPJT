from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Geinin

# Create your views here.
def index(request):
    return render(request,"index.html")


def compos(request):
    d=request.POST['q1']
    if(d=='漫才'):
        return render(request,"Manzai.html",request.POST)
    elif(d=='コント'):
        return render(request,"Konto.html",request.POST)
    if(d=='ピン'):
        return render(request,"Pin.html",request.POST)

def result(request):
    d=request.POST['q1']
    
    '''
    imp=[(float(request.POST['c1'])*float(request.POST['c2'])*float(request.POST['c3']))**(1/4),
    ((1/float(request.POST['c1']))*float(request.POST['c4'])*float(request.POST['c5']))**(1/4),
    ((1/float(request.POST['c2']))*(1/float(request.POST['c4']))*float(request.POST['c6']))**(1/4),
    ((1/float(request.POST['c3']))*(1/float(request.POST['c5']))*(1/float(request.POST['c6'])))**(1/4)]

    
    impos=[imp[i]/sum(imp)for i in range(4)]

    gs=Geinin.objects.filter(neta=d)
    max=0
    res='誰か'
    for g in gs:
        com=[g.importance1,g.importance2,g.importance3,g.importance4]
        score=sum([x*y for (x,y) in zip(com,impos)])
        if(score>max):
            max=score
            res=g.name
            link=g.Link
            image=g.image
    '''
    impos=[int(request.POST['c1']),int(request.POST['c2']),int(request.POST['c3']),int(request.POST['c4']),int(request.POST['c5']),int(request.POST['c6'])]
    gs=Geinin.objects.filter(neta=d)
    max=0
    res='誰か'

    cs=["人気度","ツッコミの怒り度","発言のおかしさ","見た目の個性","テンポ感","雰囲気"]
    if d=="コント":
        cs[0]="設定　"
        cs[1]="展開　　　　　　"
        cs[2]="共感性　　　　"
        cs[3]="シュールさ　"
        cs[4]="ボケ量　"
        cs[5]="人気度"
    elif d=="ピン":
        cs[0]="人気度"
        cs[1]="モノマネ力　　　"
        cs[2]="発言のおかしさ"
        cs[3]="クレイジーさ"
        cs[4]="複雑さ　"
        cs[5]="声量　"

    for g in gs:
        com=[g.importance1,g.importance2,g.importance3,g.importance4,g.importance5,g.importance6]
        a=sum([x*y for (x,y) in zip(com,com)])**(1/2)
        b=sum([x*y for (x,y) in zip(impos,impos)])**(1/2)
        score=sum([x*y for (x,y) in zip(com,impos)])/(a*b)

        if(score>max):
            max=score
            
            res={"score":score,
             "name":g.name,
             "link":g.Link,
             "image":g.image,
             "des":g.description,
             "type":d,
             "impos":impos,"c1":cs[0],"c2":cs[1],"c3":cs[2],"c4":cs[3],"c5":cs[4],"c6":cs[5],
            }

        if d=="ピン":
            res["image"]="https://news.mynavi.jp/article/20200803-1198503/images/001.jpg"
            return redirect("https://stat.ameba.jp/user_images/20180830/14/artstyle-shiga/a8/68/j/o3202284214257151220.jpg?caw=800")


    return render(request,"Result.html",res)