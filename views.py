from django.shortcuts import render
from django.http import JsonResponse 
from Bengkel_api.models import Bengkel

# Create your views here.
def Bengkel_list(request):
    Bengkel = Bengkel.objects.all() # Complex Data
    Bengkel_Python = list(Bengkel.values()) # python DS 
    return JsonResponse({
        'Bengkel': Bengkel_Python
    })