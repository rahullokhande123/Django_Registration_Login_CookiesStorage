from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        print(request.method)
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get(('password'))

        response=render(request,'login.html')
        response.set_cookie('name',name)
        response.set_cookie('email',email)
        response.set_cookie('contact',contact)
        response.set_cookie('password',password)
        return response
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        name1=request.COOKIES['name']
        email1=request.COOKIES['email']
        contact1=request.COOKIES['contact']
        password1=request.COOKIES['password']
        if email1==email:
            if password1==password:
                my_data={
                    'nm':name1,
                    'em':email1,
                    'con':contact1,
                    'pas':password1
                }
                return render(request,'dashboard.html',my_data)
            else:
                msg="Password Incorrect"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Not Valide"
            return render(request,'login.html',{"msg":msg})
    else:
        return render(request,"login.html")


    # if request.method=="POST":
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')

    #     data2=request.COOKIES['data1']

    #     print(data2)
        
    #     if data2['email']==email:
    #         if data2['password']==password:
    #             my_data={
    #                 'nm':data2['name'],
    #                 'em':data2['email'],
    #                 'con':data2['contact'],
    #                 'pas':data2['password']
    #             }
    #             return render(request,'dashboard.html',my_data)
    #         else:
    #              msg="Password not correct"
    #              return render (request,'login.html',{"msg":msg})           
    #     else:
    #          msg="Email not found"
    #          return render(request,"login.html",{'msg':msg})
    # else:
    #      return render(request,'login.html')

def logout(request):
        if request.COOKIES:
            response=render(request,'home.html')
            response.delete_cookie('name')
            response.delete_cookie('contact')
            response.delete_cookie('email')
            response.delete_cookie('password')
            return response
       
