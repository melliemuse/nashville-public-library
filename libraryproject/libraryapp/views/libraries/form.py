import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def library_form(request):
    if request.method == 'GET':
        template = 'libraries/form.html'
        context = {}
    return render(request, template, context)