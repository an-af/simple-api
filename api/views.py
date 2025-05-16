from django.http import JsonResponse
from .models import Customer
from django.forms.models import model_to_dict
import datetime

# testing
def test(request):
    time = datetime.datetime.now()
    response = {
        "msg" : "KeepCalm !, It works",
        "server-time" : time.strftime("%d %B %Y | %H:%M:%S WIB")
    }
    return JsonResponse(response)

# get all Data
def getAllData(request):
    try:
        data = Customer.objects.all().values('id','name','email','phone')
        print(data)
        return JsonResponse({"customers" : list(data)})
    
    except Exception as e:
        return JsonResponse({"error":str(e)}, status=500)

# get data By Id
def getDataByID(request, customer_id):
    try:
        data = Customer.objects.get(id=customer_id)
        data = model_to_dict(data)
        return JsonResponse({"data":data}, status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, status=500)
