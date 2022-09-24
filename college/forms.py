from django import forms
from .models import students , subjects , exam , tracks
import this
l = {("Male" , "Male") , ("Female" , "Female") , ("Other" , "Other")}
class studentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'


class tracksForm(forms.ModelForm):
   
    class Meta:
        model = tracks
        fields = '__all__'



class subjectsForm(forms.ModelForm):

    class Meta:
        model = subjects
        fields ='__all__'

class examForm(forms.ModelForm):
    class Meta:
        model = exam
        fields = '__all__'
