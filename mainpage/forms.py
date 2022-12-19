from django import forms
from.models import Appointments
class ShowDatePicker(forms.DateInput):
    input_type = 'date'



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields= "__all__"
        widgets = {
            'a_date':ShowDatePicker(),
        }
        labels ={
            'dept_name':'Department Name',
            'a_date':"Appointment Date"
        }