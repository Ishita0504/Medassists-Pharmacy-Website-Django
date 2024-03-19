from django.shortcuts import render
from . import Pool
from django .http import JsonResponse
def Regi_Interface(request):
    return render(request,'Register page.html')

def Submit_Registration(request):
       try:
           DB,CMD=Pool.ConnectionPooling()
           emailid = request.POST['emailid']
           password = request.POST['password']
           conpassword = request.POST['conpassword']
           profileicon = request.FILES['profileicon']
           adminname=request.POST['username']
           Q="insert into regis  (emailid,password,conpassword,profileicon,adminname) values('{0}','{1}','{2}','{3}','{4}')".format(emailid,password,conpassword,profileicon.name,adminname)
           F=open("d:/medassist_ecom/assests/"+profileicon.name,'wb')
           for chunk in profileicon.chunks():
               F.write(chunk)
           F.close()
           CMD.execute(Q)
           DB.commit()
           DB.close()
           if(password==conpassword):

              return render(request, 'Register page.html',{'message':'CREATED...'})
           else:

               return render(request, 'Register page.html', {'message': 'PASSWORD IS NOT SAME '})
       except Exception as e:
                 print("errorssubmit:",e)
                 return render(request,'Register page.html',{'message':'FAIL TO SUBMIT THE RECORD'})