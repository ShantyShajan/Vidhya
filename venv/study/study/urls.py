"""kalariproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studyapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('', index),
    path('about', about),
    path('courseview', courseview),
    path('contact', contact),
    path('login', login),  
    path('register', register),
    path('editac',editac),
     path('editprof/<int:id>', editprof),
    path('treg', treg),
    path('ereg', ereg),
    path('manreg', manreg),
    path('studhome', studhome),
    path('adminhome', adminhome),
    path('thome', thome),
    path('manhome', manhome),
    path('ehome', ehome),
    path('manview', manview),
    path('teachview', teachview),
    path('exview', exview),
    path('editex/<int:id>', editex),
    path('dltex/<int:id>', dltex),
    path('editeach/<int:id>', editeach),
    path('dlteach/<int:id>', dlteach),
    path('studregview', studregview),
    path('dltstud/<int:id>', dltstud),
    path('editman/<int:id>', editman),
    path('dltman/<int:id>', dltman),
    path('manaview1', manaview1),
    path('studcomp', studcomp),
    path('tcomp_response/<int:id>',tcomp_response),
    # path('compla_responseview/<int:id>',compla_responseview),
    path('deletecomp/<int:id>', deletecomp),
    path('dltcomp/<int:id>', dltcomp),
    path('teachcomp', teachcomp),
    path('studcompview/<int:id>', studcompview),
    path('tcompview', tcompview),
    path('adcourse', adcourse),
    # path('deleteecourse/<int:id>',deleteecourse),
    path('courseview', courseview),
    path('mcourseview', mcourseview),
    path('joboff', joboff),
    path('applyjob/<int:id>', applyjob),
    path('addjob', addjob),
    path('dltjob/<int:id>', dltjob),
    path('jobview', jobview),
    path('studchat/<int:id>', studchat),
    path('teachlistview',teachlistview),
    path('chatview',chatview),
    path('response/<int:id>',response),
    path('tutorial',tutorial),
    path('tutorialview',tutorialview),
    path('tutviewteach',tutviewteach),
    path('editvideo/<int:id>', editvideo),
    path('dltvid/<int:id>', dltvid),
    path('addmeet',addmeet),
    path('studmeet',studmeet),
    path('tmeetview',tmeetview),
    path('editmeet/<int:id>',editmeet),
    path('dltvideo/<int:id>', dltvideo),
    path('tresponseview',tresponseview),
    path('addtimetable',addtimetable),
    path('timetabview',timetabview),
    path('edittimetable/<int:id>',edittimetable),
    path('dltt/<int:id>', dltt),
    path('viewtimet',viewtimet),
    path('admintimet',admintimet),
    path('tcomp_response',tcomp_response),
    # path('studcomp_response',studcomp_response),
    path('adcomplaintview',adcomplaintview),
    path('upload',upload),
    path('uploadqp',uploadqp),
    path('deleteqp/<int:id>', deleteqp),
    path('uploadqb',uploadqb),
    path('qpview',qpview),
    path('qbview',qbview),
    path('teachqpview',teachqpview),
    path('teachqbview',teachqbview),
    path('editexamm/<int:id>',editexamm),
    path('dltexam/<int:id>', dltexam),
    path('studexamview',studexamview),
    path('addexam',addexam),
    path('midterm',midterm),
    path('midterm',midterm),
    path('logout', logout),
    path('respond/<int:id>',respond),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

