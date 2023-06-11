from django.shortcuts import render
# below are my lines
from django.http import HttpResponse
# Create your views here.
def home(request): # this is a route
    return render(request,"index.html")
  #  return HttpResponse("""<h1>Hey I am a Django Server</h1>"
  #                      <p>Hey this is coming from server</p>
  #                      <h3>hope you are well</h3>
                        
  #                      """)


def  success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey this is a success page</h1>")