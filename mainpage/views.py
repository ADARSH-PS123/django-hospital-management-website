from django.shortcuts import render

from.models import Department,Doctor,Appointments
from.forms import AppointmentForm

def home(request):
    numbers={"nums":[1,2,3,4,5,6,7,8]}
    return render(request,'home.html',numbers)
def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')
def doctors(request):
    data = {"doctors":Doctor.objects.all()}
    return render(request,'doctors.html',data)
def contact(request):
    return render(request,'contact.html')
def departmets(request):
    depa={'depts': Department.objects.all()}
    return render(request,'departments.html',depa)
def createAppointment(request):
    form = AppointmentForm()
    appointments = Appointments.objects.all()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'alert.html')
    return render(request,"appointment.html",{'form':form,'latestAppointments':appointments})




