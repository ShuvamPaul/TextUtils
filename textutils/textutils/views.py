# I have created this file - Tony
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def navigate(request):
    return HttpResponse('''<h1>Navigate from here</h1><br/>
        <a href="https://www.youtube.com/">Go to you tube
        </a><br/>
        <a href="https://www.google.co.in/">Go to google
        </a><br/>
        <a href="https://www.wikipedia.org/">Wiki anything!
        </a><br/>
        ''')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        puncuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in puncuations:
                analyzed += char
        params = {'purpose': 'remove puncuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            params = {'purpose': 'removed newline', 'analyzed_text': analyzed}
            djtext = analyzed

    if spaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'removed spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
        params = {'purpose': 'character count', 'analyzed_text': count}
        djtext = count

    if removepunc != 'on' and fullcaps != "on" and newlineremover != 'on' and spaceremover != 'on' and charcount != 'on' :
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
