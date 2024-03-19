from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def SubCategory_Interface(request):
    return render(request,'subcategoryinterface.html')
@xframe_options_exempt
def Submit_SubCategory(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        subcategoryname = request.POST['subcategoryname']
        subcategoryicon = request.FILES['subcategoryicon']
        Q = "insert into subcategories (categoryid ,subcategoryname,subcategoryicon) values('{0}','{1}','{2}')".format(categoryid,subcategoryname,subcategoryicon.name)
        F = open("d:/medassist_ecom/assests/" + subcategoryicon.name, 'wb')
        for chunk in subcategoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'subcategoryinterface.html', {'message': 'RECORD SUBMITTED SUCCESSFULLY'})
    except Exception as e:
        print("error:", e)
        return render(request, 'subcategoryinterface.html', {'message': 'FAIL TO SUBMIT THE RECORD'})
@xframe_options_exempt
def Display_All_SubCategory(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'login page.html')

    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select * from subcategories"
        CMD.execute(Q)
        record=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllSubCategories.html',{'record':record})
    except Exception as e:
           print('error',e)
           return render(request,'DisplayAllSubCategories.html',{'record':None})
@xframe_options_exempt
def Edit_SubCategory(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        subcategoryname = request.GET['subcategoryname']
        subcategoryid = request.GET['subcategoryid']

        Q = "update subcategories set subcategoryname='{0}' where  subcategoryid={1}".format(subcategoryname,subcategoryid)

        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print('error', e)
        Display_All_SubCategory(request)
        return JsonResponse({'message':'FAIL TO EDIT'})
@xframe_options_exempt
def Delete_SubCategory(request):
    try:
       DB,CMD=Pool.ConnectionPooling()
       subcategoryid = request.GET['subcategoryid']
       Q="delete from subcategories  where  subcategoryid={0}".format(subcategoryid)
       print(Q)
       CMD.execute(Q)
       DB.commit()
       DB.close()
       return JsonResponse({'result':True},safe=False)
    except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_SubCategoryIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        subcategoryid=request.POST['subcategoryid']
        subcategoryicon = request.FILES['subcategoryicon']
        Q = "update subcategories set subcategoryicon='{0}' where subcategoryid={1} ".format(subcategoryicon.name,subcategoryid)
        print(Q)
        F = open("d:/medassist_ecom/assests/" + subcategoryicon.name, 'wb')
        for chunk in subcategoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        Display_All_SubCategory(request)
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('erroredit', e)
        Display_All_SubCategory(request)
        return JsonResponse({'result': False}, safe=False)
