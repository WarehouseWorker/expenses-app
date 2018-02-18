from django.shortcuts import render

def exp_list(request):
    return render(request, 'expform/exp_list.html', {})