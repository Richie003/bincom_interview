from django.http import HttpResponse, JsonResponse
import datetime
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
    party_results = Announced_pu_results.objects.all()
    context = {
        'form':form,
         'party_data': party_results
    }
    return render(request, 'party_result.html', context)

def addPartyResult(request):
    if request.method == "POST":
        id_data = request.POST.get('puu')
        party_abbr = request.POST.get('pa')
        party_score_data = request.POST.get('ps')
        user = request.POST.get('user')
        date = datetime.datetime.now()
        ipaddr = request.POST.get('ipadd')
        create_result = Announced_pu_results.objects.create(
            polling_unit_uniqueid = id_data,
            party_abbreviation = party_abbr,
            party_score=party_score_data,
            entered_by_user = user,
            date_entered = date,
            user_ip_address = ipaddr
        )
        create_result.save()
        success = f'Result added successfully for {party_abbr} by {user} on {date.date()}'
    return HttpResponse(success)