#created by Abid Khan
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    # return  HttpResponse('<h1>Home</h1>')

def analyzed(request):
    djtext = request.POST.get('text', 'default')
    djremovepunc = request.POST.get('removepunc', 'off')
    djuppercase = request.POST.get('fullcap', 'off')
    djnewlineremove =request.POST.get('newlineremove', 'off')
    djextraspaceremover =request.POST.get('extraspaceremover', 'off')
    djcharacter =request.POST.get('charactercounter', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if djremovepunc == "on":
        djanalyzed = ""
        for char in djtext:
            if char not in punctuations:
                djanalyzed = djanalyzed + char
        djtext = djanalyzed
        # params = {'purpose': 'Removed Punctuations', 'analyzed_text': djanalyzed}
    if(djuppercase == 'on'):
        djanalyzed = ""
        for char in djtext:
            djanalyzed =djanalyzed + char.upper()
        # params = {'purpose': 'UPPER CASE', 'analyzed_text': djanalyzed}
        djtext = djanalyzed
    if (djnewlineremove == 'on'):
        djanalyzed = ""
        for char in djtext:
            if (char != '\n'and char != '\r'):
                djanalyzed =djanalyzed + char
        djtext = djanalyzed
        # params = {'purpose': 'New Line Removed', 'analyzed_text': djanalyzed}
    if (djextraspaceremover == 'on'):
        djanalyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                djanalyzed = djanalyzed +char
        # params = {'purpose': 'Extra Space Removed', 'analyzed_text': djanalyzed}
        djtext = djanalyzed
    # if (djcharacter == 'on'):
    #     num = 0
    #     for char in djtext:
    #         if not (char == " "):
    #             num += 1
    # djtext = djanalyzed
    params = {'purpose': 'Total Character in Text', 'analyzed_text': djanalyzed}
    # else:
    #    djanalyzed = "error"

    return  render(request,'analyzed.html', params)



# def capfirst(request):
#     return  HttpResponse("capitalize first letter")
#
# def newlineremover(request):
#     return  HttpResponse("new line remover")

