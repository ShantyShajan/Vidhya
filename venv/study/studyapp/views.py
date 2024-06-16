from django.shortcuts import render

from urllib import request
from django.shortcuts import render,redirect
from studyapp.models import *
#import os
import smtplib
from studyapp.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def index(request):
   return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def courseview(request):
   return render(request,'courseview.html')

def studhome(request):
   return render(request,'studhome.html')

def adminhome(request):
   return render(request,'adminhome.html')

def thome(request):
   return render(request,'thome.html')

def ehome(request):
   return render(request,'ehome.html')

def manhome(request):
   return render(request,'manhome.html')

def manview(request):
   return render(request,'manview.html')

def teachview(request):
   return render(request,'teachview.html')

def exview(request):
   return render(request,'exview.html')
   
def manaview1(request):
   return render(request,'manaview1.html')

def adcourse(request):
   return render(request,'adcourse.html')
def courseview(request):      
   return render(request,'courseview.html') 

def contact(request):      
   return render(request,'contact.html')

def studlayout(request):      
   return render(request,'studlayout.html')

def joboff(request):      
   a = jobs.objects.filter().all()
   return render(request,'joboff.html',{'a':a}) 

def applyjob(request,id):
   res =jobs.objects.get(id=id)
   jobid = res.id
   print(jobid)
   if request.method == 'POST':
      uid = request.session['userid']
      name = request.POST.get('name')
      address = request.POST.get('address')
      dob = request.POST.get('dob')
      email = request.POST.get('email')
      gender = request.POST.get('gender')
      mobile = request.POST.get('mobile')
      qualification = request.POST.get('qualification')
      experience = request.POST.get('experience')
      specialization = request.POST.get('specialization')
      year = request.POST.get('year')
      data = applyjobs.objects.create(jobid=jobid,uid=uid,name=name,address=address,dob=dob,email=email,gender=gender,mobile=mobile,qualification=qualification,experience=experience,specialization=specialization,year=year)
      return redirect('/studhome')       
   return render(request,'applyjob.html')

def logout(request):
   request.session.flush()
   return redirect('/')
# def logout(request):
#    request.session.flush()
#    logout(request)
#    messages.success(request,
#    '<p>You were successfully logout</p>')
#     return redirect('/')
def register(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      dob = request.POST.get('dob')
      gender = request.POST.get('gender')
      mobile = request.POST.get('mobile')
      email = request.POST.get('email')
      course = request.POST.get('course')
      board = request.POST.get('board')
      password = request.POST.get('password')
      cpass = request.POST.get('cpass')   
      if password == cpass:
        data = reg.objects.create(name=name,dob=dob,gender=gender,email=email,mobile=mobile,course=course,board=board,password=password,usertype="student")
        return redirect('/login') 
      else:
         a = "Password does not match !"
         return render(request,'reg.html',{'a':a})        
   return render(request,'reg.html') 

def treg(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      gender = request.POST.get('gender')
      email = request.POST.get('email')
      mobile = request.POST.get('mobile')
      course = request.POST.get('course')
      qualification = request.POST.get('qualification')
      experience = request.POST.get('experience')
      password = request.POST.get('password')
      cpass = request.POST.get('cpass')   
      if password == cpass:
         data = reg.objects.create(name=name,gender=gender,email=email,mobile=mobile,course=course,qualification=qualification,experience=experience,password=password,usertype="teacher")
         return redirect('/teachview')
      else:
         a = "Password does not match !"
         return render(request,'treg.html',{'a':a})        
   return render(request,'treg.html')

def ereg(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      gender = request.POST.get('gender')
      email = request.POST.get('email')
      mobile = request.POST.get('mobile')
      course = request.POST.get('course')
      qualification = request.POST.get('qualification')
      experience = request.POST.get('experience')
      password = request.POST.get('password')
      cpass = request.POST.get('cpass')   
      if password == cpass:
         data = reg.objects.create(name=name,gender=gender,email=email,mobile=mobile,course=course,qualification=qualification,experience=experience,password=password,usertype="examiner")
         return redirect('/exview') 
      else:
         a = "Password does not match !"
         return render(request,'ereg.html',{'a':a})        
   return render(request,'ereg.html')

def manreg(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      gender = request.POST.get('gender')
      email = request.POST.get('email')
      mobile = request.POST.get('mobile')
      qualification = request.POST.get('qualification')
      experience = request.POST.get('experience')
      password = request.POST.get('password')
      cpass = request.POST.get('cpass')   
      if password == cpass:
         data = reg.objects.create(name=name,gender=gender,email=email,mobile=mobile,qualification=qualification,experience=experience,password=password,usertype="manager")
         return redirect('/manview') 
      else:
         a = "Password does not match !"
         return render(request,'manreg.html',{'a':a})        
   return render(request,'manreg.html')

def contact(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      data = contacts.objects.create(name=name,email=email,subject=subject,message=message)
      return redirect('/contact')   
   return render(request,'contact.html') 
   
def login(request):
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      if reg.objects.filter(email=email,password=password):
         data = reg.objects.get(email=email,password=password)
         if data.usertype == "student":
            request.session['userid']=data.id
            return redirect('/studhome')
         if data.usertype == "admin":
            request.session['adminid']=data.id
            return redirect('/adminhome')    
         if data.usertype == "teacher":
            request.session['tid']=data.id
            print(data.id)
            return redirect('/thome')
         if data.usertype == "examiner":
            request.session['eid']=data.id
            return redirect('/ehome')  
         if data.usertype == "manager":
            request.session['mid']=data.id
            return redirect('/manhome')    
   return render(request,'login.html')

def manview(request):      
   a = reg.objects.filter(usertype="manager").all()
   return render(request,'manview.html',{'a':a})

def editman(request,id):
   res = reg.objects.get(id=id)
   if request.method == "POST":
      res.name = request.POST.get('name')
      res.email = request.POST.get('email')
      res.gender = request.POST.get('gender')
      res.mobile = request.POST.get('mobile')
      res.qualification = request.POST.get('qualification')
      res.experience = request.POST.get('experience')
      res.save()
      return redirect('/manview')
   return render(request,'editman.html',{'res':res})

def dltman(request,id):
   res = reg.objects.get(id=id)
   res.delete()  
   return redirect('/manview')

def teachview(request):      
   a = reg.objects.filter(usertype="teacher").all()
   return render(request,'teachview.html',{'a':a})
def editeach(request,id):
   res = reg.objects.get(id=id)
   if request.method == "POST":
      res.name = request.POST.get('name')
      res.email = request.POST.get('email')
      res.gender = request.POST.get('gender')
      res.mobile = request.POST.get('mobile')
      res.course = request.POST.get('course')
      res.qualification = request.POST.get('qualification')
      res.experience = request.POST.get('experience')
      res.save()
      return redirect('/teachview')
   return render(request,'editeach.html',{'res':res})

def studregview(request):      
   a = reg.objects.filter(usertype="student").all()
   return render(request,'studregview.html',{'a':a})

def dltstud(request,id):
   res = reg.objects.get(id=id)
   res.delete()  
   return redirect('/studregview')

def editac(request):
   sid = request.session['userid']
   print(sid)
   res =reg.objects.get(id=sid)
   if request.method == 'POST':
      res.name = request.POST.get('name')
      res.dob = request.POST.get('dob')
      res.gender = request.POST.get('gender')
      res.mobile = request.POST.get('mobile')
      res.email = request.POST.get('email')
      res.course = request.POST.get('course')
      res.board = request.POST.get('board')
      res.password = request.POST.get('password')
      res.cpass = request.POST.get('cpass')
      return redirect('/editprof')
   return render(request,'editac.html',{'res':res})

def editprof(request,id):
   sid = request.session['userid']
   print(sid)
   res =reg.objects.get(id=sid)
   if request.method == 'POST':
      res.name = request.POST.get('name')
      res.dob = request.POST.get('dob')
      res.gender = request.POST.get('gender')
      res.mobile = request.POST.get('mobile')
      res.email = request.POST.get('email')
      res.course = request.POST.get('course')
      res.board = request.POST.get('board')
      res.password = request.POST.get('password')
      res.save()
      return redirect('/editac')
   return render(request,'editprof.html',{'res':res})

def dlteach(request,id):
   res = reg.objects.get(id=id)
   res.delete()  
   return redirect('/teachview')

def exview(request):      
   a = reg.objects.filter(usertype="examiner").all()
   return render(request,'exview.html',{'a':a})

def editex(request,id):
   res = reg.objects.get(id=id)
   if request.method == "POST":
      res.name = request.POST.get('name')
      res.email = request.POST.get('email')
      res.gender = request.POST.get('gender')
      res.mobile = request.POST.get('mobile')
      res.course = request.POST.get('course')
      res.qualification = request.POST.get('qualification')
      res.experience = request.POST.get('experience')
      res.password = request.POST.get('password')
      res.confirmpassword = request.POST.get('cpass')
      res.save()
      return redirect('/exview')
   return render(request,'editex.html',{'res':res})

def dltex(request,id):
   res = reg.objects.get(id=id)
   res.delete()  
   return redirect('/exview')

def studcomp(request):
   if request.method == 'POST':
      uid = request.session['userid']
      print(uid)
      subject = request.POST.get('subject')
      complaint = request.POST.get('complaint')
      data = complaints.objects.create(uid=reg.objects.get(id=uid),subject=subject,complaint=complaint,usertype="student")
      return redirect('/studcomp')       
   return render(request,'studcomp.html') 

def deletecomp(request,id):
      res = complaints.objects.get(id=id)
      res.delete()
      return redirect('/adcomplaintview',{'res':res})

def teachcomp(request):
   if request.method == 'POST':
      uid = request.session['tid']
      print(uid)
      subject = request.POST.get('subject')
      complaint = request.POST.get('complaint')
      data = complaints.objects.create(uid=reg.objects.get(id=uid),subject=subject,complaint=complaint,usertype="teacher")
      return redirect('/teachcomp')       
   return render(request,'teachcomp.html')

def dltcomp(request,id):
   res = complaints.objects.get(id=id)
   res.delete()  
   return redirect('/tcompview')

def tcompview(request):   
   a = complaints.objects.filter(usertype="teacher").all()
   return render(request,'tcompview.html',{'a':a})

def studcompview(request):
   a = complaints.objects.filter(usertype="student").all()
   return render(request,'studcompview.html',{'a':a})

def adcourse(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      description = request.POST.get('description')
      data = course.objects.create(name=name,description=description)
      return redirect('/manhome')       
   return render(request,'adcourse.html')
   
   # def deleteecourse(request,id):
   #    res = course.objects.get(id=id)
   #    res.delete()  
   # return redirect('/tutviewteach')  

def courseview(request):      
   a = course.objects.filter().all()
   return render(request,'courseview.html',{'a':a})

def addjob(request): 
   if request.method == 'POST':
      job = request.POST.get('job')
      institution = request.POST.get('institution')
      location = request.POST.get('location')
      salary = request.POST.get('salary')
      description= request.POST.get('description')
      data = jobs.objects.create(job=job,institution=institution,location=location,salary=salary,description=description)
      return redirect('/addjob')       
   return render(request,'addjob.html')

def jobview(request):      
   a = applyjobs.objects.all()
   return render(request,'jobview.html',{'a':a})
def dltjob(request,id):
   res = applyjobs.objects.get(id=id)
   res.delete()  
   return redirect('/jobview')

def mcourseview(request):
   a = course.objects.all()
   return render(request,'mcourseview.html',{'a':a})

def teachlistview(request):
   a = reg.objects.filter(usertype="teacher").all()   
   return render(request,'teachlistview.html',{'a':a})

def studchat(request,id):
   res =reg.objects.get(id=id)
   tid = res.id
   print(tid)
   if request.method == 'POST':
      sid = request.session['userid']
      message = request.POST.get('message')
      data = chat.objects.create(tid=tid,sid=reg.objects.get(id=sid),message=message)
      return redirect('/studhome')   
   return render(request,'studchat.html') 

def chatview(request):
   print("-----")
   tid =  request.session['tid']
   print("-----")
   print(tid)
   a = chat.objects.filter(status="null",tid=tid).all()
   return render(request,'chatview.html',{'a':a}) 

def response(request,id):
   res =chat.objects.get(id=id)
   if request.method == 'POST':
      res.response = request.POST.get('message')
      res.status="complete"
      res.save()
      return redirect('/thome')   
   return render(request,'response.html',{'res':res}) 

def tutorial(request):
   if request.method == "POST":
      up = video()
      up.date = request.POST.get('date')
      up.subject = request.POST.get('subject')
      up.classes = request.POST.get('classes')
      # up.userid = request.session['userid']
      # up.name = request.session['uname']
      if len(request.FILES) != 0:
         up.video = request.FILES['video']
         up.save()
         return redirect('/tutviewteach')
   return render(request, 'tutorial.html')

def tutorialview(request):      
   a = video.objects.filter().all()
   return render(request,'tutorialview.html',{'a':a})

def tutviewteach(request):      
   a = video.objects.filter().all()
   return render(request,'tutviewteach.html',{'a':a})

def editvideo(request,id):
   res = video.objects.get(id=id)
   if request.method == "POST":
      res.date = request.POST.get('date')
      res.subject = request.POST.get('subject')
      res.classes = request.POST.get('classes')
      res.video = request.POST.get('video')
      res.save()
      return redirect('/tutviewteach')
   return render(request,'editvideo.html',{'res':res})

def dltvid(request,id):
   res = video.objects.get(id=id)
   res.delete()  
   return redirect('/tutviewteach')

def addmeet(request):
   if request.method == 'POST':
      date = request.POST.get('date')
      time = request.POST.get('time')
      subject = request.POST.get('subject')
      classes = request.POST.get('classes')
      link = request.POST.get('link')
      data = meet.objects.create(date=date,time=time,subject=subject,classes=classes,link=link)
      return redirect('/tmeetview')  
   return render(request,'addmeet.html')

def studmeet(request):      
   a = meet.objects.filter().all()
   return render(request,'studmeet.html',{'a':a})

def tmeetview(request):      
   a = meet.objects.filter().all()
   return render(request,'tmeetview.html',{'a':a})

def editmeet(request,id):
   res = meet.objects.get(id=id)
   if request.method == "POST":
      res.date = request.POST.get('date')
      res.time = request.POST.get('time')
      res.subject = request.POST.get('subject')
      res.classes = request.POST.get('classes')
      res.link = request.POST.get('link')
      res.save()
      return redirect('/tmeetview')
   return render(request,'editmeet.html',{'res':res})

def dltvideo(request,id):
   res = meet.objects.get(id=id)
   res.delete()  
   return redirect('/tmeetview')

def tresponseview(request):
   sid = request.session['userid']      
   a = chat.objects.filter(sid=sid).all()
   return render(request,'tresponseview.html',{'a':a})

def timetabview(request):      
   a = ttable.objects.all()
   return render(request,'timetabview.html',{'a':a})

def edittimetable(request,id):
   res = ttable.objects.get(id=id)
   if request.method == "POST":
      res.examname = request.POST.get('examname')
      res.classe = request.POST.get('classe')
      res.date = request.POST.get('date')
      res.time = request.POST.get('time')
      res.subject = request.POST.get('subject')
      res.save()
      return redirect('/timetabview')
   return render(request,'edittimetable.html',{'res':res})

def dltt(request,id):
   res = ttable.objects.get(id=id)
   res.delete()  
   return redirect('/timetabview')

def viewtimet(request):      
   a = ttable.objects.all()
   return render(request,'viewtimet.html',{'a':a})

def admintimet(request):      
   a = ttable.objects.all()
   return render(request,'admintimet.html',{'a':a})

def tcomp_response(request,id):
   res = complaints.objects.get(id=id)
   uid =res.id
   print(uid)
   a = res.uid
   print(a)
   e = a.email
   print(e)
   if request.method == 'POST':
      messages = request.POST.get('response')
      email = e
      print(email)
      print(messages)
      subject = 'welcome arya'
      message = messages
      print(message)
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]
      send_mail(subject,message,email_from,recipient_list)
      res.respond ="RESPONSE"
      res.save()
      return redirect('/adminhome')
   return render(request,'tcomp_response.html',{'res':res})

def adcomplaintview(request):
   a = complaints.objects.all()
   return render(request,'adcomplaintview.html',{'a':a})

def uploadqp(request):
   if request.method == "POST":
      up = uploads()
      up.classe = request.POST.get('classe')
      up.subject = request.POST.get('subject')
      up.year = request.POST.get('year')
      up.mtype="qpaper"
      if len(request.FILES) != 0:
         up.browse = request.FILES['browse']
         up.save()
         return redirect('/teachqpview')
   return render(request, 'uploadqp.html')

def deleteqp(request,id):
   res = uploads.objects.get(id=id)
   print(res)
   res.delete()  
   return redirect('/teachqpview',{'res':res})

def uploadqb(request):
   if request.method == "POST":
      up = uploads()
      up.classe = request.POST.get('classe')
      print(up.classe)
      up.subject = request.POST.get('subject')
      print(up.subject)
      up.year = request.POST.get('year')
      print(up.year)
      up.mtype="qbank"
      print("--------------------")
      if len(request.FILES) != 0:
         up.browse = request.FILES['browse']
         print("--------------------")
         print(up.browse)
         up.save()
         return redirect('/teachqbview')
   return render(request, 'uploadqb.html')

def qpview(request):      
   a = uploads.objects.filter(mtype="qpaper").all()
   return render(request,'qpview.html',{'a':a})

def teachqpview(request):      
   a = uploads.objects.filter(mtype="qpaper").all()
   return render(request,'teachqpview.html',{'a':a})

def qbview(request):      
   a = uploads.objects.filter(mtype="qbank").all()
   return render(request,'qbview.html',{'a':a})

def teachqbview(request):      
   a = uploads.objects.filter(mtype="qbank").all()
   return render(request,'teachqbview.html',{'a':a})

def addexam(request):
   if request.method == 'POST':
      classe = request.POST.get('classe')
      subject = request.POST.get('subject')
      date = request.POST.get('date')
      time = request.POST.get('time')
      link = request.POST.get('link')
      data = exam.objects.create(classe=classe,subject=subject,date=date,time=time,link=link)
      return redirect('/ehome')       
   return render(request,'addexam.html')

def eexamview(request):      
   a = exam.objects.all()
   return render(request,'eexamview.html',{'a':a})

def editexamm(request,id):
   res = exam.objects.get(id=id)
   if request.method == "POST":
      res.classe = request.POST.get('classe')
      res.subject = request.POST.get('subject')
      res.date = request.POST.get('date')
      res.time = request.POST.get('time')
      res.link = request.POST.get('link')
      res.save()
      return redirect('/editexamm')
   return render(request,'editexamm.html',{'res':res})

def dltexam(request,id):
   res = exam.objects.get(id=id)
   res.delete()  
   return redirect('/editexam')

def studexamview(request):      
   a = exam.objects.all()
   return render(request,'studexamview.html',{'a':a})

def addtimetable(request):
   if request.method == 'POST':
      classe = request.POST.get('classe')
      ddate = request.POST.get('adate')
      time = request.POST.get('time')
      subject = request.POST.get('subject')
      data = ttable.objects.create(classe=classe,ddate=ddate,time=time,subject=subject)
      return redirect('/timetabview')
   return render(request,'addtimetable.html')

def upload(request):
   return render(request,'upload.html')

def midterm(request):
   if request.method == 'POST':
      ddate = request.POST.get('ddate')
      time = request.POST.get('time')
      subject = request.POST.get('subjectn')
      data = ttable.objects.create(ddate=ddate,time=time,subject=subject)
      return redirect('/manhome') 
   return render(request,'midterm.html')

def respond(request,id):
   res = complaints.objects.get(id=id)
   uid =res.id
   print(uid)
   a = res.tid
   print(a)
   e = a.email
   print(e)
   if request.method == 'POST':
      messages = request.POST.get('res')
      email = e
      print(email)
      print(messages)
      subject = 'welcome arya'
      message = messages
      print(message)
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]
      send_mail(subject,message,email_from,recipient_list)
      res.respond ="RESPONSE"
      res.save()
      return redirect('/adminhome')
   return render(request,'respond.html')

