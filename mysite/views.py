#ksndfojnfoknf
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def analyse(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitilize=request.POST.get('capitilize','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    analysed=""
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':"Removing Punctuations",'analysed_text':analysed}

    if capitilize=='on':
        if len(analysed)>1:
            djtext=analysed
            analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        params={'purpose':"capitilize letters",'analysed_text':analysed}

    if newlineremover=='on':
        if len(analysed)>1:
            djtext=analysed
            analysed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analysed=analysed+char
        params={'purpose':"new line remover",'analysed_text':analysed}

    if extraspaceremover=='on':
        if len(analysed)>1:
            djtext=analysed
            analysed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analysed = analysed + char
        params={'purpose':"extra space remover",'analysed_text':analysed}

    if charactercounter=='on':
        if len(analysed)>1:
            djtext=analysed
            analysed=""
        count=0
        for char in djtext:
            if char==" ":
                pass
            else:
                count=count+1
        params={'purpose':"character counter",'analysed_text':djtext,'counter':"count ="+str(count)}

    if removepunc == 'on' or capitilize == 'on' or newlineremover == 'on' or extraspaceremover == 'on'or charactercounter=='on':
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse('Select any operation and try again')
