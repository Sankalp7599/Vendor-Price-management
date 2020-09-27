from django.shortcuts import render
from django.http import HttpResponse
def showTest(request):
    que="who invent india?"
    a="columbus"
    b="vasco"
    c="akbar"
    d="rama devi"
    level="EASY"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(request):

    return HttpResponse
