from django.shortcuts import render
from django.http import HttpResponse

posts = [
    
    
    {

            'author':'Kush',
            'title':'Blog Post 1',
            'content':'First post content',
            'date_posted':'August 5 , 2021'
    
},

{

            'author':'Kush',
            'title':'Blog Post 2',
            'content':'second post content',
            'date_posted':'August 5 ,2021'


}

]
# Create your views here.


def home(request):
    context = {

            'posts':posts,
            'title': 'Home'

    }
    return render(request, 'blog/home.html' , context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})