from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def ResultIndex(request):
    polling_obj = Polling_unit.objects.all()[:1]
    lga_obj = LGA.objects.all()
    context = {
        'data':polling_obj,
        'lga_data': lga_obj
    }
    return render(request, 'index.html', context)

def get_lga(request):
    if request.method == 'POST':
        choice =request.POST.get('user_choice')
        choice = int(choice)
        obj = Polling_unit.objects.filter(lga_id=choice)
        return JsonResponse({'data': len(obj)})


def PartyIndex(request, *args, **kwargs):
    form = Announced_pu_results_form
    context = {'form':form}
    return render(request, 'example2.html', context)