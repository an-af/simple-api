from django.http import JsonResponse

# Create your views here.

def hello_world(request):
    return JsonResponse({"msg" : "Haii semuaa...."})
