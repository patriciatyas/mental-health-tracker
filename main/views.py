from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152241',
        'name': 'Patricia Herningtyas',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
