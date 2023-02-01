from django.shortcuts import render
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
    for g in gs:
        com=[g.importance1,g.importance2,g.importance3,g.importance4,g.importance5,g.importance6]
        a=sum([x*y for (x,y) in zip(com,com)])**(1/2)
        b=sum([x*y for (x,y) in zip(impos,impos)])**(1/2)
        score=sum([x*y for (x,y) in zip(com,impos)])/(a*b)
        if(score>max):
            max=score
            res=g.name
            link=g.Link
            image=g.image
            des=g.description

    return render(request,"Result.html",{'name':res,'link':link,'image':image,'impos':impos,'type':d,'score':max,'des':des})