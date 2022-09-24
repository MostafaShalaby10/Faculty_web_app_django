from this import d
from django.shortcuts import render
from .models import students, subjects, tracks, exam
from .forms import studentsForm, subjectsForm, examForm, tracksForm


def home(request) :
    return render(request , "home.html")

def showstudents(request):
    data = students.objects.raw('select s.id ,s.name , s.age , s.mail ,s.phone , s.gender , t.track_name from college_students s join college_tracks t on s.track_id_id = t.id ')
    return render(request, 'showstudents.html', {"stu": data})


def showsubjects(request):
    return render(request, 'showsubjects.html', {"sub": subjects.objects.all()})


def showexams(request):
    data = exam.objects.raw('select e.id , e.score , e.date , s.id , t.id from college_students s join college_exam e on e.student_id_id = s.id join college_subjects t on e.subject_id_id = t.id ;')
    return render(request, 'showexams.html', {"ex": data})


def showtracks(request):
    data = tracks.objects.raw("select t.id , t.track_name , s.id from  college_tracks t join college_subjects s  on t.subject_id_id = s.id ")
    return render(request, 'showtracks.html', {"tra": tracks.objects.all()})


def insertstudents(request):
    if request.method == "POST":
        data = studentsForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, "insertstudents.html", {"f": studentsForm})


def insertsubjects(request):
    if request.method == "POST":
        data = subjectsForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, "insertsubjects.html", {"f": subjectsForm})


def inserttracks(request):
    if request.method == "POST":
        data = tracksForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, "inserttracks.html", {"f": tracksForm})


def insertexam(request):
    if request.method == "POST":
        data = examForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, "insertexam.html", {"f": examForm})


def editstudents(request, id):
    data = studentsForm(instance=students.objects.get(id=id))
    return render(request, "editstudents.html", {"edit": data})


def editsubjects(request, id):
    data = subjectsForm(instance=subjects.objects.get(id=id))
    return render(request, "editsubjects.html", {"edit": data})


def editexam(request, id):
    data = examForm(instance=exam.objects.get(id=id))
    return render(request, "editexam.html", {"edit": data})


def edittracks(request, id):
    data = tracksForm(instance=tracks.objects.get(id=id))
    return render(request, "edittracks.html", {"edit": data})

def updatestudents(request , id) :
    if request.method=="POST":
        data = studentsForm(request.POST , instance=students.objects.get(id=id))
        if data.is_valid() :
            data.save()
            return render(request , "update.html" , {"f": students.objects.get(id=id)} )
        else : 
            return render(request , "showstudents.html" , {"f": students.objects.get(id=id)} )

def updatesubjects(request , id) :
    if request.method=="POST":
        data = subjectsForm(request.POST , instance=subjects.objects.get(id=id))
        if data.is_valid() :
            data.save()
            return render(request , "update.html" , {"f": subjects.objects.get(id=id)} )
        else : 
            return render(request , "showsubjects.html" , {"f": subjects.objects.get(id=id)} )

def updatetracks(request , id) :
    if request.method=="POST":
        data = tracksForm(request.POST , instance=tracks.objects.get(id=id))
        if data.is_valid() :
            data.save()
            return render(request , "update.html" , {"f": tracks.objects.get(id=id)} )
        else : 
            return render(request , "showtracks.html" , {"f": tracks.objects.get(id=id)} )

def updateexam(request , id) :
    if request.method=="POST":
        data = examForm(request.POST , instance=exam.objects.get(id=id))
        if data.is_valid() :
            data.save()
            return render(request , "update.html" , {"f": exam.objects.get(id=id)} )
        else : 
            return render(request , "showstudents.html" , {"f": exam.objects.get(id=id)} )

def deletestudents(request , id) :
    data = students.objects.get(id=id)
    data.delete()
    return render(request , "showstudents.html" , {"f" : students.objects.all()})

def deletesubjects(request , id) :
    data = subjects.objects.get(id=id)
    data.delete()
    return render(request , "showsubjects.html" , {"f" : subjects.objects.all()})

def deleteexam(request , id) :
    data = exam.objects.get(id=id)
    data.delete()
    return render(request , "showexams.html" , {"f" : exam.objects.all()})

def deletetracks(request , id) :
    data = tracks.objects.get(id=id)
    data.delete()
    return render(request , "showtracks.html" , {"f" : tracks.objects.all()})
# Create your views here.
