from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Category_Interface(request):
    try:
        admin = request.session['ADMIN']
        return render(request, 'categoryinterface.html')
    except:
        return render(request, 'login page.html')
@xframe_options_exempt
def Submit_Category(request):
       try:
           DB,CMD=Pool.ConnectionPooling()
           categoryname=request.POST['categoryname']
           categoryicon=request.FILES['categoryicon']
           Q="insert into categories (categoryname,categoryicon) values('{0}','{1}')".format(categoryname,categoryicon.name)
           F=open("d:/medassist_ecom/assests/"+categoryicon.name,'wb')
           for chunk in categoryicon.chunks():
               F.write(chunk)
           F.close()

           CMD.execute(Q)
           DB.commit()
           DB.close()
           return render(request, 'categoryinterface.html',{'message':'RECORD SUBMITTED SUCCESSFULLY'})
       except Exception as e:
              print("error:",e)
              return render(request,'categoryinterface.html',{'message':'FAIL TO SUBMIT THE RECORD'})

@xframe_options_exempt
def Display_All_Category(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'login page.html')

    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select * from categories"
        CMD.execute(Q)
        record=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllCategories.html',{'record':record})
    except Exception as e:
           print('error',e)
           return render(request,'DisplayAllCategories.html',{'record':None})

def Edit_Category(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        categoryname = request.GET['categoryname']
        Q = "update categories set categoryname='{0}' where categoryid='{1}'".format(categoryname,categoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        Display_All_Category(request)
        return JsonResponse({'result':True},safe=False)

    except Exception as e:
        print('error', e)
        Display_All_Category(request)
        return JsonResponse({'result':False}, safe=False)
@xframe_options_exempt
def Delete_Category(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        categoryname = request.GET['categoryname']
        Q = "delete from categories where categoryid='{0}' ".format(categoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        Display_All_Category(request)
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print('error', e)
        Display_All_Category(request)
        return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def Fetch_All_Category_JSON(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        Q = "select * from categories"
        CMD.execute(Q)
        records = CMD.fetchall()
        DB.close()
        return JsonResponse({'data': records}, safe=False)
    except Exception as e:
        print('Error:', e)
        return render(request, 'DisplayAllCategories.html', {{'data': None}})

@xframe_options_exempt
def Edit_CategoryIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        categoryicon = request.FILES['categoryicon']
        Q = "update categories set categoryicon='{0}' where categoryid={1} ".format(categoryicon.name,categoryid)
        print(Q)
        F = open("d:/medassist_ecom/assests/" + categoryicon.name, 'wb')
        for chunk in categoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        Display_All_Category(request)
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('error', e)
        Display_All_Category(request)
        return JsonResponse({'result':False}, safe=False)


