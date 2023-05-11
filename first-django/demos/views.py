from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작입니다.')

    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'request.__dict__ = {request.__dict__}')

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    return render(request, 'calculator.html', {'result':result})