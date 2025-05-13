from django.http import JsonResponse
import datetime 

# Logika 
def new_hello_worlds(request):
    return JsonResponse({"pesan" : "hai semua...."})


def waktu_sekarang(request):
    waktu = datetime.datetime.now()
    format_waktu = waktu.strftime("%d %B %Y, %H:%M:%S WIB")
    return JsonResponse({"jam_sekarang" :format_waktu })