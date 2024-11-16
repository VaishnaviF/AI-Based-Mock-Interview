

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import cv2, os
from .models import *
from django.shortcuts import render, redirect
from .Evaluation import calculate_cnn_accuracy
from django.http import HttpResponse
from openpyxl import Workbook
from io import BytesIO
# Create your views here.

def homepage(request):

    return render(request, 'index.html',{})

def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.POST['aid']
    pwd=request.POST['pwd']
    print(userid, pwd,'')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        
        return render(request, 'adminhome.html',{} )
        
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html', {'b':False})

def usersignup(request):
    return render(request, 'user.html', {'b':True})

def usignupaction(request):
    if request.method == 'POST':
        email = request.POST['mail']

        d = users.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'user.html', {'msg': "Email Already Registered"})
        else:
            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            city = request.POST['city']
            name = request.POST['name']
            age = request.POST['age']
            gen = request.POST['gen']

            d = users(name=name, email=email, pass_word=pass_word, phone=phone, gender=gen, city=city,  age=age)
            d.save()

        return render(request, 'user.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'user.html')

def userloginaction(request):
    if request.method=='POST':
        uid=request.POST['mail']
        pass_word=request.POST['pass_word']
        d=users.objects.filter(email__exact=uid).filter(pass_word__exact=pass_word).count()
        
        if d>0:
            d=users.objects.filter(email__exact=uid)
            request.session['email']=uid
            request.session['name']=d[0].name
         
         
            return render(request, 'user_home.html',{'data': d[0]})

        else:
            return render(request, 'user.html',{'msg':"Login Fail"})

    else:
        return render(request, 'user.html')
    

def userlogout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def userhome(request):
    if "email" in request.session:
        email=request.session["email"]
        d=users.objects.filter(email__exact=email)

       
        return render(request, 'user_home.html',{'data': d[0]})

    else:
        return redirect('userlogout')



def training(request):
    if request.method=='POST':
        from .Training import build_cnnmodel
        build_cnnmodel()
        return render(request, 'training.html',{'msg':'Training process completed !! '})
    else:
        return render(request, 'training.html')
   

  
def evaluation(request):
    if request.method=='POST':
        
        graph, lst=calculate_cnn_accuracy()
        data={'a':lst[0], 'p':lst[1], 'r':lst[2],'f':lst[3]}
        return render(request, 'eval.html',{'image_base64': graph,'data':data, 'b':True})
    else:
        return render(request, 'eval.html')
   


def datasetpage(request):
    return render(request, 'datasetpage.html')


import csv
import random

def upload(request):
    if "adminid" in request.session:
        file = request.POST['file']
        q_a_dataset.objects.all().delete()
        with open(file, 'r') as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['Question'], i['Answer'], i['Subject'], i['Category']) for i in dr]
            for l in to_db:
                category = l[3]
                subject = l[2] if category in ['Technical', 'Behavioral'] else None
                d = q_a_dataset(question=l[0], answer=l[1], subject=subject, category=category)
                d.save()
        return render(request, 'datasetpage.html', {'msg': "Dataset Uploaded Successfully"})
    else:
        return render(request, 'admin.html')

def examinit(request):
    if "email" in request.session:
        email = request.session["email"]

        if request.method == "POST":
            selected_category = request.POST.get('category')
            subjects = q_a_dataset.objects.filter(category=selected_category).values('subject').distinct()
            return render(request, 'examinit.html', {'subjects': subjects, 'selected_category': selected_category})

        else:
            categories = q_a_dataset.objects.values('category').distinct()
            return render(request, 'examinit.html', {'categories': categories})

    else:
        return redirect('userlogout')



from .DateDetails import getdate
def examstart(request):
    category = request.POST['category']
    if category == 'Technical':
        sub = request.POST['sub']
        questions = q_a_dataset.objects.filter(category=category, subject=sub).order_by('?')
    else:
        sub = request.POST['sub']  # Now also getting subject for Behavioral
        questions = q_a_dataset.objects.filter(category=category, subject=sub).order_by('?')
    
    first_question = questions.first()
    request.session['qidlist'] = [first_question.id]
    request.session['qid'] = first_question.id
    request.session['category'] = category
    if category == 'Technical':
        request.session['sub'] = sub
    eid = random.randint(9999, 99999)
    request.session['eid'] = eid
    dt = getdate()

    e = exam(eid=eid, name=request.session["name"], email=request.session["email"], category=category, subject=sub, date_time=dt, result='')
    e.save()

    return render(request, 'examstart.html', {'data': first_question})

def answerpro(request):
    
    que=request.POST['que']
    qid=request.POST['qid']

    exp=faceexp()
    request.session["exp"]=exp
    d=q_a_dataset.objects.filter(id=qid)
    d=d[0]

    
    return render(request, 'examstart2.html',{'data': d})


def answerpro2(request):
    from .speech import main
    main('C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\msg.txt')
    
    f1 = open('msg.txt')
    ans = f1.read()
    
    que = request.POST['que']
    qid = request.POST['qid']
    email = request.session["email"]

    exp = request.session["exp"]
    score1 = 0.3
    if exp == 'Happy' or exp == 'Surprise':
        score1 = 1.0
    elif exp == 'Neutral':
        score1 = 0.6
    score1 = score1 * 30

    eid = request.session["eid"]
        
    d = q_a_dataset.objects.filter(id=qid)
    d = d[0]
        
    oanswer = d.answer

    from .StringCompare import jaccard_similarity
    score3 = jaccard_similarity(oanswer, ans)
    score3 = score3 * 50

    from .Grammer import grammer_check

    gans = grammer_check(ans)
    score2 = jaccard_similarity(gans, ans)
    score2 = score2 * 20

    # Generate feedback based on scores
    feedback = generate_feedback(score1, score2, score3)  # Create this function to generate feedback

    # Save the question's data in examdata
    exam_data = examdata(eid=eid, qid=qid, question=d.question, faceexp=exp, sc1=score1, answer=ans, sc2_g=score2, sc3_m=score3)
    exam_data.save()

    # Calculate the total score for the exam
    all_exam_data = examdata.objects.filter(eid=eid)  # Query all questions for this exam
    if all_exam_data.exists():
        total_score = sum(float(data.sc1) + float(data.sc2_g) + float(data.sc3_m) for data in all_exam_data)
        total_questions = len(all_exam_data)
        exam.objects.filter(eid=eid).update(result=total_score / total_questions if total_questions > 0 else 0)

    return render(request, 'examstart2.html', {'data': exam_data, 'feedback': feedback})




def generate_feedback(score1, score2, score3):
    feedback = ""
    if score1 > 25:
        feedback += "Good emotional response! "
    else:
        feedback += "Consider relaxing your emotions. "

    if score2 > 15:
        feedback += "Your grammar is on point! "
    else:
        feedback += "Try to improve your grammar. "

    if score3 > 30:
        feedback += "You answered well! "
    else:
        feedback += "Try to improve your response quality. "

    return feedback



import time
def faceexp():
    cam = cv2.VideoCapture(0)
    cam.set(1, 40)
    cam.set(1, 80)
    i=0
    while i<3:
        ret, img = cam.read()
        cv2.imshow('Capture', img)
        cv2.imwrite(filename="cameraimg"+str(i)+".jpg", img=img)
        k = cv2.waitKey(10) & 0xff
        time.sleep(1)
        i=i+1

    print("\n close camera")
    cam.release()
    cv2.destroyAllWindows()

    full_file_path = os.path.join('cameraimg1.jpg')
    from .Prediction import predict_emo
    emo=predict_emo()

    return emo

def uviewresult(request):
    if "email" in request.session:
        email = request.session['email']
        d = exam.objects.filter(email=email)

        return render(request, 'uviewresult.html', {'data': d})

    else:
        return render(request, 'user.html')



def viewdetail(request):
    if "email" in request.session:
        eid=request.GET['eid']
        
        d = examdata.objects.filter(eid=eid)


        return render(request, 'viewresult.html', {'data': d})

    else:
        return render(request, 'user.html')



def aviewresult(request):
    if "adminid" in request.session:
        d = exam.objects.filter()

        return render(request, 'aviewresult.html', {'data': d})

    else:
        return render(request, 'admin.html')

from .models import exam  # Assuming you have an ExamResult model that stores exam details

def delete_exam_result(request):
    if request.method == "POST":
        eid = request.POST.get('eid')  # Get the exam id from the form

        # Assuming your model is called ExamResult and eid is a unique field
        try:
            result = exam.objects.get(eid=eid)
            result.delete()  # Delete the record from the database
            return redirect('/aviewresult/')  # Redirect to the results page after deletion
        except exam.DoesNotExist:
            return HttpResponse("Exam result does not exist", status=404)
    else:
        return HttpResponse("Invalid request method", status=400)

def aviewdetail(request):
    if "adminid" in request.session:
        eid=request.GET['eid']
        
        d = examdata.objects.filter(eid=eid)


        return render(request, 'aviewresult2.html', {'data': d})

    else:
        return render(request, 'admin.html')


