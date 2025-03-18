from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# 회원가입
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
        else:
            messages.error(request, '회원가입에 실패했습니다. 다시 시도해주세요.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 로그인
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, '로그인 성공!')
            return redirect('todo_list')  # 로그인 후 To-Do List 페이지로 이동
        else:
            messages.error(request, '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

