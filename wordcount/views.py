from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("hello!")
    return render(request, 'home.html', {'hi_there': 'yo yo chiki chiki'})

def about(request):
    return render(request, 'about.html')



def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist),'worddictionary':worddictionary.items()})

# def cool(reqest):
#     return HttpResponse("<h1>i am cool</h1>");
