import json
from django.http import JsonResponse
from .models import Customer
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import datetime

# testing
def test(request):
    time = datetime.datetime.now()
    response = {
        "msg" : "KeepCalm !, It works",
        "server-time" : time.strftime("%d %B %Y | %H:%M:%S WIB")
    }
    return JsonResponse(response)

# get all & post Data 
@csrf_exempt 
def getAllData(request):
    try:
        if request.method == 'GET':
            data = Customer.objects.all().values('id','name','email','phone')
            return JsonResponse({"customers" : list(data)}, status=200)
        else: 
            # receive & process data
            temp = json.loads(request.body.decode('UTF-8'))
            data = {
                'name' : temp.get('name'),
                'email' : temp.get('email'),
                'phone' : temp.get('phone'),
            }
            # save data
            customerData = Customer(**data) 

            customerData.save()

            return JsonResponse({"msg" : "data saved !", "data" : data},status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, status=500)

# get data By Id
@csrf_exempt
def operationDataByID(request, customer_id):
    try:
        # get data by id
        if request.method == 'GET': 
            data = Customer.objects.get(id=customer_id)
            data = model_to_dict(data)
            return JsonResponse({"data":data}, status=200)
        # delete data by id
        if request.method == 'DELETE':
            data = Customer.objects.get(id=customer_id)
            data.delete()
            return JsonResponse({"msg":'delete data success'}, status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, status=500)
    
# edit data
@csrf_exempt
def updateData(request, customer_id):
    try:
        if request.method == 'PATCH':
            customer = Customer.objects.get(id = customer_id)
            temp  = json.loads(request.body.decode('UTF-8'))
            customer.name = temp['name']
            customer.email = temp['email']
            customer.phone = temp['phone']
            print(customer)
            
            responseData = {
                'name' : customer.name,
                'email' : customer.email,
                'phone' : customer.phone
            }
            return JsonResponse({"status" : "OK", "data" : responseData}, status = 200)
        else:
            return JsonResponse({"msg" : "method not allowed"}, status = 405)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status = 404)
    except Exception as msg:
        return JsonResponse({"error": str(msg)}, status = 500)