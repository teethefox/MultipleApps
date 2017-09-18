from django.shortcuts import render, HttpResponse,redirect
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
def new(request):
    response="new new"
    return HttpResponse(response)
def create(request):
    return redirect('/blogs')

def show(request, blog_id):
    print blog_id
    return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))
    
def delete(request, blog_id):
    return redirect('/blogs')

# Create your views here.
