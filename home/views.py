from django.shortcuts import render
# below are my lines
from django.http import HttpResponse
# Create your views here.
def home(request): # this is a route
    peoples = [
        {'name':'GuruBoy','age': 26},
        {'name':'GalliBoy','age': 36},
        {'name':'Vicky','age': 46},
        {'name':'John','age': 16},
        {'name':'Don','age': 66},
    ]

    return render(request,"index.html", context = {'peoples': peoples})
  #  return HttpResponse("""<h1>Hey I am a Django Server</h1>"
  #                      <p>Hey this is coming from server</p>
  #                      <h3>hope you are well</h3>
                        
  #                      """)


def  success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey this is a success page</h1>")