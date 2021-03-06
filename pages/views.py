from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm,Registrationform
from django.contrib.auth import authenticate, login
import os
from django.contrib.auth.models import User
from .models import UserProfile, LogTimes
import datetime
from django.contrib.auth import logout
from PIL import Image
from django.urls import path, include
import face_recognition
import cv2 
from django.contrib.sessions.models import Session

def facedect(loc):
        cam = cv2.VideoCapture(0)
        print(cam)
        s, img = cam.read()
        
        if s:   
                
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                MEDIA_ROOT =os.path.join(BASE_DIR,'pages')
                print(loc)
                loc=(str(MEDIA_ROOT)+loc)
                
                Image.open(loc)
                print("loc from media root"+loc)
                face_1_image = face_recognition.load_image_file(loc)
                face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

                #

                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                print("face lcations",face_locations)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                
                
                check=face_recognition.compare_faces([face_1_face_encoding], face_encodings)
                
                top, right, bottom, left =(face_recognition.face_locations(img))[0]
                
                print("found face at top:{}, left:{}, bottom:{}, right:{}".format(top,left,bottom,right))
                face_image=img[top:bottom,left:right]
                pill_image=Image.fromarray(face_image)
                pill_image.save("face.jpg")
                
                print(check)
                print(check[0])
                if check[0]:
                        return True

                else :
                        return False    

def about(request):
    return render(request,"about.html",context)

def base(request):
        if request.session.has_key('uid'):
            return redirect('index')
        if request.method =="POST":
                form =LoginForm(request.POST)
                if form.is_valid():
                        username=request.POST['email']
                        password=request.POST['password']
                        user = authenticate(request,username=username,password=password)
                        
                        if user is not None:
                                print(user.userprofile.head_shot.url)
                                if facedect(user.userprofile.head_shot.url):
                                        login(request,user)
                                        request.session['uid']=True
                                        val=str(user)                                       
                                        var1=UserProfile.objects.get(user=User.objects.get(username=val).id)
                                        print(var1)
                                        mon=var1.logtimes_set.create(login_time=datetime.datetime.now())
                                        mon.save()
                                return redirect('index')
                        else:
                                return redirect('index')        
        else:
                MyLoginForm = LoginForm()
                return render(request,"base.html",{"MyLoginForm": MyLoginForm})  

def home(request):
    user=LogTimes.objects.all()
    context={'user':user}
    return render(request, 'home.html', context)

#from django.contrib.auth.forms import UserCreationForm

def logout_request(request):
    logout(request)
    if 'uid' in request.session:
        del request.session['uid']
    
    return render(request,'registration/logout.html')

def index(request):
    if request.session.has_key('uid'):
        return render(request,"index.html",{})
    else:
        return redirect('base')

def register(request):
        if request.method =="POST":
                form =Registrationform(request.POST)
                if form.is_valid():
                        form.save()
                        username=form.cleaned_data['username']
                        password=form.cleaned_data['password1']
                        user = authenticate(username=username,password=password)
                        login(request,user)
                        return redirect('index')
                else:
                        return redirect('index')        

        form =Registrationform()
        return render(request,'registration/register.html',{'form':form})        

def profile(request):
        return render(request,'profile.html',{})

def notallowed(request):
        return render(request,'notallowed.html',{})

def common(request):
        return render(request,'common.html',{})