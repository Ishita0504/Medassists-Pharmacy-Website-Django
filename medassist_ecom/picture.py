from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def  picture(request):
    return render(request ,'picture.html')
@xframe_options_exempt
def submitpicture(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandid = request.POST['brandid']
        productid = request.POST['productid']
        icon = request.FILES['icon']
        Q = "insert into picture( categoryid,subcategoryid, brandid,productid,icon) values('{0}','{1}','{2}''{3}','{4}')".format(categoryid,subcategoryid,brandid,productid, icon.name)
        F = open("g:/medassist_ecom/assests/" + icon.name, 'wb')
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'picture.html', {'message': 'RECORD SUBMITTED SUCCESSFULLY'})
    except Exception as e:
        print("error:", e)
        return render(request, 'picture.html', {'message': 'FAIL TO SUBMIT THE RECORD'})
