from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Brand_Interface(request):
    return render(request,'brandinterface.html')
@xframe_options_exempt
def Submit_Brand(request):
       try:
           DB,CMD=Pool.ConnectionPooling()
           categoryid = request.POST['categoryid']
           subcategoryid = request.POST['subcategoryid']
           brandname = request.POST['brandname']
           person = request.POST['person']
           mobileno = request.POST['mobileno']
           status = request.POST['status']
           brandicon = request.FILES['brandicon']
           Q="insert into brands(categoryid,subcategoryid,brandname,person,mobileno,logo,status) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,subcategoryid,brandname,person,mobileno,brandicon.name,status)
           F=open("d:/medassist_ecom/assests/"+brandicon.name,'wb')
           for chunk in brandicon.chunks():
               F.write(chunk)
           F.close()
           CMD.execute(Q)
           DB.commit()
           DB.close()
           return render(request, 'brandinterface.html',{'message':'RECORD SUBMITTED SUCCESSFULLY'})
       except Exception as e:
              print("errorssubmit:",e)
              return render(request,'brandinterface.html',{'message':'FAIL TO SUBMIT THE RECORD'})
@xframe_options_exempt
def Display_All_brand(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'login page.html')

    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select b.*,(select c.categoryname from categories c where c.categoryid=b.categoryid) as cname,(select s.subcategoryname from subcategories s where b.subcategoryid=s.subcategoryid) as scname from brands b"
        CMD.execute(Q)
        record=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllBrands.html',{'record':record})
    except Exception as e:
           print('errordisplay',e)
           return render(request,'DisplayAllBrands.html',{'record':None})

@xframe_options_exempt
def Fetch_All_SubCategory_JSON(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        q = "select * from subcategories where categoryid={0}".format(categoryid)
        print(q)
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()

        return JsonResponse({'data': records}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'data': None}, safe=False)
@xframe_options_exempt
def Delete_Brand(request):
    try:
       DB,CMD=Pool.ConnectionPooling()
       brandid= request.GET['brandid']
       Q="delete from brands  where brandid={0}".format(brandid)
       print(Q)
       CMD.execute(Q)
       DB.commit()
       DB.close()
       return JsonResponse({'result':True},safe=False)
    except Exception as e:
      print("Errorofdelete:",e)
      return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Edit_Brand(request):
   try:
        DB, CMD = Pool.ConnectionPooling()
        brandid = request.GET['brandid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        brandname = request.GET['brandname']
        person = request.GET['person']
        mobileno = request.GET['mobileno']

        Q = "update brands set brandname='{0}',categoryid={1},subcategoryid={2},person='{3}',mobileno='{4}' where brandid={5}".format(brandname,categoryid,subcategoryid,person,mobileno,brandid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)
   except Exception as e:
       print('errordit', e)
       Display_All_brand(request)
       return JsonResponse({'message': 'FAIL TO EDIT'})
@xframe_options_exempt
def Edit_BrandIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        brandid=request.POST['brandid']
        brandicon = request.FILES['brandicon']
        Q = "update brands set  logo='{0}' where brandid={1} ".format(brandicon.name,brandid)
        print(Q)
        F = open("d:/medassist_ecom/assests/" +brandicon.name, 'wb')
        for chunk in brandicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        Display_All_brand(request)
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('erroredit', e)
        Display_All_brand(request)
        return JsonResponse({'result': False}, safe=False)
