from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
def Login_Interface(request):
    return render(request,'login page.html')
def Admin_Logout(request):
    del request.session['ADMIN']
    return render(request,"login page.html")


def Submit_Login(request):
    try:
       DB, CMD = Pool.ConnectionPooling()
       emailid= request.POST['emailid']
       password = request.POST['password']
       Q="select * from regis where emailid='{0}' and password='{1}'".format(emailid,password)
       CMD.execute(Q)
       record=CMD.fetchone()
       if(record):
              request.session['ADMIN'] = record
              return render(request,'Dashboard.html',{'AdminData': record})
       else:
         return render(request,'login page.html', {'message': 'INAVLID EMAILD/PASSWORD'})
       DB.close()
    except Exception as e:
        print("errorslogin:", e)
        return render(request, 'login page.html', {'message': 'FAIL TO LOGIN THE RECORD'})



