from django import forms
from .models import Todo
from django_summernote.widgets import SummernoteWidget  # summernote 위젯 import

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed', 'completed_image']  # 필요한 필드들만 선택

    # Summernote를 description 필드에 사용
    description = forms.CharField(widget=SummernoteWidget())

    # Bootstrap 클래스 추가
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

