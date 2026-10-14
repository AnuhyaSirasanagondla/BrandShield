import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import BrandProfile, Detection

def dashboard(request): return render(request, 'monitoring/index.html')
@require_GET
def health(request): return JsonResponse({'status':'ok','service':'BrandShield API','mode':'prototype'})
@require_GET
def detections(request):
    qs = Detection.objects.order_by('-score')
    return JsonResponse({'count':qs.count(),'results':[{'id':d.id,'name':d.name,'handle':d.handle,'channel':d.get_channel_display(),'risk':d.risk,'score':d.score,'status':d.status,'signals':d.signals,'reason':d.reason} for d in qs]})
@csrf_exempt
@require_POST
def run_scan(request):
    """Creates a clearly labelled demo scan dataset; no external platform is queried."""
    samples = [
      {'name':'Northstar Pay Support','handle':'@northstar_helpdesk','channel':'social','risk':'High','score':94,'signals':['Name similarity','Added support term','Handle not allowlisted'],'reason':'The display name resembles the configured brand and adds a support-related term. This is a heuristic signal, not proof of abuse.'},
      {'name':'Northstar Pay Wallet','handle':'Publisher: QuickFunds Labs','channel':'app','risk':'High','score':91,'signals':['App name similarity','Publisher mismatch'],'reason':'The app title resembles the configured brand but its publisher differs from the trusted publisher reference.'},
      {'name':'North Star Pay','handle':'@north_star_pay','channel':'social','risk':'Medium','score':72,'signals':['Spacing variation','Handle not allowlisted'],'reason':'A spacing variation and unknown handle were found. Verify manually before escalation.'},
    ]
    created=[]
    for item in samples:
        d=Detection.objects.create(**item)
        created.append({'id':d.id,'name':d.name,'risk':d.risk,'score':d.score,'signals':d.signals})
    return JsonResponse({'message':'Demo scan complete. No live platform was queried.','created':created,'count':len(created)}, status=201)
@csrf_exempt
@require_POST
def brand_profile(request):
    try: data=json.loads(request.body or '{}')
    except json.JSONDecodeError: return HttpResponseBadRequest('Invalid JSON')
    profile=BrandProfile.objects.first() or BrandProfile()
    for field in ('brand_name','website','official_handles','official_publisher'):
        if field in data: setattr(profile,field,str(data[field])[:500])
    profile.save()
    return JsonResponse({'saved':True,'brand_name':profile.brand_name,'website':profile.website,'official_handles':profile.official_handles,'official_publisher':profile.official_publisher})
