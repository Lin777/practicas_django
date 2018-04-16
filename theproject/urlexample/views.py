from django.http import HttpResponse
# Create your views here.
def profile(request, username="Default user"):
    return HttpResponse('<h1>This is the profile page! The user is {}</h1>'.format(username))

def article(requset, article='50'):
    return HttpResponse('<h1>The article name is: {}</h1>'.format(article))