from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('userhome/', views.userhome, name="userhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    path('userlogout/', views.userlogout, name="userlogout"),
    
    path('training/', views.training, name="training"),
    path('evaluation/', views.evaluation, name="evaluation"),
    path('eval/', views.evaluation, name="eval"),

    path('datasetpage/', views.datasetpage, name="datasetpage"),
    path('upload/', views.upload, name="upload"),  # Handles dataset upload with category field

    path('examinit/', views.examinit, name="examinit"),  # Category selection page
    path('examstart/', views.examstart, name="examstart"),  # Start the exam based on category
    

    path('answerpro/', views.answerpro, name="answerpro"),
    path('answerpro2/', views.answerpro2, name="answerpro2"),

    path('uviewresult/', views.uviewresult, name="uviewresult"),
    path('viewdetail/', views.viewdetail, name="viewdetail"),
    path('aviewresult/', views.aviewresult, name="aviewresult"),
    path('delete_exam_result/', views.delete_exam_result, name='delete_exam_result'),
    path('aviewdetail/', views.aviewdetail, name="aviewdetail"),
]
