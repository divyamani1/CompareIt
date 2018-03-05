from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.files import File
import difflib
import os

def get_default(file_name):
    if os.path.isfile(file_name + '.txt'):
        default_file = open(file_name + '.txt', 'r')
        default_text = default_file.read()
        return default_text
    return ''

def Home_view(request):
    default_original_text = get_default('original')
    default_user_text = get_default('user')
    return render(request, 'index.html',{'default_original_text': default_original_text, 'default_user_text': default_user_text})

def post_original(request):
    if request.method == 'GET':
        redirect(Home_view)
        messages.warning(request, 'Please submit text again.')
    if request.method == 'POST':
        otext = request.POST.get('Original-text')
        with open('original.txt', 'w') as original_file:
            original_file.write(otext)
        original_file.close()
        messages.success(request, 'Text saved successfully.')
    return redirect(Home_view)

def post_user(request):
    if request.method == 'GET':
        redirect(Home_view)
        messages.warning(request, 'Please submit text again.')
    if request.method == 'POST':
        utext = request.POST.get('User-text')
        with open('user.txt', 'w') as user_file:
            user_file.write(utext)
        user_file.close()
        messages.success(request, 'Text saved successfully.')
    return redirect(Home_view)

def report_view(request):
    if request.method == 'GET':
        redirect(Home_view)
        messages.warning(request, 'You need to submit both texts first.')
    if request.method == 'POST':
        original_file = 'original.txt'
        user_file = 'user.txt'
        if not os.path.isfile(original_file) or not os.path.isfile(user_file):
            messages.error(request, "File doesn't exist. Please submit the texts first.")
            return redirect(Home_view)
        original_file_lines = open('original.txt', 'r').readlines()
        user_file_lines = open('user.txt', 'r').readlines()
        diff_html_unformatted = difflib.HtmlDiff().make_table(original_file_lines, user_file_lines, original_file, user_file)
        return render(request, 'report.html', {'diff_html_table': diff_html_unformatted})
    return redirect(Home_view)