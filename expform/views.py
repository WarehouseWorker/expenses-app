from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Spend
from .forms import SpendForm

def exp_list(request):
    spend_list = Spend.objects.filter(created_data__lte=timezone.now()).order_by('-created_data')
    return render(request, 'expform/exp_list.html', {'spend_list': spend_list})

def exp_detail(request, pk):
    spend = get_object_or_404(Spend, pk=pk)
    return render(request, 'expform/exp_detail.html', {'spend': spend})

def exp_new(request):
    if request.method == "POST":
        form = SpendForm(request.POST)
        if form.is_valid():
            spend = form.save(commit=False)
            spend.author = request.user
            spend.created_data = timezone.now()
            spend.save()
            return redirect('exp_detail', pk=spend.pk)
    else:
        form = SpendForm()
    return render(request, 'expform/exp_edit.html', {'form': form})