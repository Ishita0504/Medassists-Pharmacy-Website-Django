from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
def  web(request):
    return render(request ,'webpage.html')

def FetchWeb(request):
    try:
      DB, CMD = Pool.ConnectionPooling()
      Q = "select * from web"
      CMD.execute(Q)
      records = CMD.fetchall()
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)