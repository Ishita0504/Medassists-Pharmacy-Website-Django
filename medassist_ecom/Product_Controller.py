from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Product_Interface(request):
    return render(request,'productinterface.html')
@xframe_options_exempt
def Fetch_All_Brand_JSON(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        q = "select * from brands where categoryid={0} and subcategoryid={1}".format(categoryid,subcategoryid)
        print(q)
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()
        return JsonResponse({'data': records}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'data': None}, safe=False)
@xframe_options_exempt
def Fetch_All_Product_JSON(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        brandid=request.GET['brandid']
        q = "select * from products where categoryid={0} and subcategoryid={1} and brandid={2} ".format(categoryid,subcategoryid,brandid)
        print(q)
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()

        return JsonResponse({'data': records}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'data': None}, safe=False)

@xframe_options_exempt
def Display_All_Product(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'login page.html')

    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid) as cname,(select s.subcategoryname from subcategories s where p.subcategoryid=s.subcategoryid) as scname,(select b.brandname from brands b where p.brandid=b.brandid) as bname from products p"
        CMD.execute(Q)
        record=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllproducts.html',{'record':record})
    except Exception as e:
           print('errordisplay',e)
           return render(request,'DisplayAllproducts.html',{'record':None})
@xframe_options_exempt
def Submit_Product(request):
    try:
        DB, CMD = Pool.ConnectionPooling()

        categoryid=request.POST['categoryid']
        subcategoryid=request.POST['subcategoryid']
        brandid=request.POST['brandid']
        productname=request.POST['productname']
        price=request.POST['price']
        offerprice=request.POST['offerprice']
        packingtype=request.POST['packingtype']
        qty=request.POST['qty']
        rating=request.POST['rating']
        salestatus=request.POST['salestatus']
        status=request.POST['status']
        producticon=request.FILES['producticon']

        Q="insert into products(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,status,salestatus,producticon,qty,rating) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,status,salestatus,producticon.name,qty,rating)
        F = open("d:/medassist_ecom/assests/" + producticon.name, 'wb')
        for chunk in producticon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'productinterface.html', {'message': 'RECORD SUBMITTED SUCCESSFULLY'})
    except Exception as e:
        print("errorssubmit:", e)
        return render(request, 'productinterface.html', {'message': 'FAIL TO SUBMIT THE RECORD'})


@xframe_options_exempt
def Delete_Product(request):
    try:
       DB,CMD=Pool.ConnectionPooling()
       productid = request.GET['productid']

       Q = "delete from products where productid={0}".format(productid)
       print(Q)
       CMD.execute(Q)
       DB.commit()
       DB.close()
       return JsonResponse({'result': True}, safe=False)
    except Exception as e:
        return JsonResponse({'result': False}, safe=False)

@xframe_options_exempt
def Edit_Product(request):
   try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        brandid = request.GET['brandid']
        productname = request.GET['productname']
        price = request.GET['price']
        offerprice = request.GET['offerprice']
        packingtype = request.GET['packingtype']
        qty = request.GET['qty']
        salestatus = request.GET['salestatus']
        status = request.GET['status']
        rating=request.GET['rating']
        productid = request.GET['productid']
        Q =  "update products set categoryid={0},subcategoryid={1},brandid={2},productname='{3}',price={4},offerprice='{5}',packingtype='{6}',status='{7}',salestatus='{8}',qty={9},rating='{10}' where productid={11}".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,status,salestatus,qty,rating,productid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)
   except Exception as e:
        print("erroredit:", e)
        return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def Edit_ProductIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        productid = request.POST['productid']
        producticon = request.FILES['producticon']
        Q = "update  products set  producticon='{0}' where productid={1} ".format(producticon.name, productid)
        print(Q)
        F = open("d:/medassist_ecom/assests/" + producticon.name, 'wb')
        for chunk in producticon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        Display_All_Product(request)
        return JsonResponse({'result': True}, safe=False)
    except Exception as e:
        print('erroredit', e)
        Display_All_Product(request)
        return JsonResponse({'result': False}, safe=False)
