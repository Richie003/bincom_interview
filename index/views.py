from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def ResultIndex(request):
    polling_obj = Polling_unit.objects.all()[:1]
    lga_obj = L
    context = {'data':polling_obj}
    return render(request, 'index.html', context)

def get_lga(request):
    if request.method == 'POST':
        choice =request.POST.get('user_choice')
        # obj = Polling_unit.objects.filter(choice)
        return JsonResponse({'data': choice}, safe=False)
