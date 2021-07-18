# I have created this file - Swastik

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def add_purpose(old_purpose, new_purpose):
    if old_purpose != "":
        return old_purpose + " and " + new_purpose
    else:
        return new_purpose


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    purpose = ""
    some_more_text = ""
    if removepunc == "on":
        temp = ""
        for char in djtext:
            if char not in punctuations:
                temp += char
        purpose = add_purpose(purpose, "Removed Punctuations")
        djtext = temp

    if fullcaps == "on":
        djtext = djtext.upper()
        purpose = add_purpose(purpose, "Changed to UPPER CASE")

    if newlineremove == "on":
        djtext = djtext.replace("\n", "")
        djtext = djtext.replace("\r", "")
        purpose = add_purpose(purpose, "Removed New Lines")

    if extraspaceremove == "on":
        purpose = add_purpose(purpose, "Removed Extra Spaces")
        temp = ""
        for index, char in enumerate(djtext):
            if (djtext[index] != " ") or temp == "" or (djtext[index] == " " and temp[-1] != " "):
                temp += char
        djtext = temp

    if charcount == "on":
        some_more_text = f"Total number of characters are {len(djtext)}."
        purpose = add_purpose(purpose, "Counted the Characters")

    params = {'purpose': purpose, 'analyzed_text': djtext,
              'some_more_text': some_more_text}
    return render(request, 'analyze.html', params)
