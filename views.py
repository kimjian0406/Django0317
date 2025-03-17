from django.shortcuts import render
from django.views.generic import CreateView
from .models import Todo
from .forms import TodoForm  # TodoForm을 import해야 합니다.

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm  # form_class를 TodoForm으로 설정
    template_name = 'todo_create.html'  # 사용할 템플릿
    success_url = '/todos/'  # 성공 시 이동할 URL

