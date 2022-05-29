from re import M
from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    #return HttpResponse("Hello there")
    data = {
        'movies':[
            {
                'id':5,
                'title':'Jaws',
                'year':1669
            },

            {
                'id':6,
                'title':'Sharknado',
                'year':1600
            },

            {
                'id':7,
                'title':'The Meg',
                'year':2000

            }

            
            
            ],

        }
    return render(request, 'movies/movies.html', data) # The request, The template to be rendered, and The Context passed tothe template to be rendered
def home(request):
    return HttpResponse("Home Page")
