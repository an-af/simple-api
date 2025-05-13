from django.http import JsonResponse
import datetime

def test(request):
    time = datetime.datetime.now()
    response = {
        "msg" : "KeepCalm !, It works",
        "server-time" : time.strftime("%d %B %Y | %H:%M:%S WIB")
    }
    return JsonResponse(response)

def getAllData(request):
    return JsonResponse({"msg":"getAllData"})
