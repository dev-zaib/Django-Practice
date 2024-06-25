from django.shortcuts import render
from .models import Create
# Create your views here.
def create_home(request):
  creates = Create.objects.all()
  return render(request, 'create_index.html', {'creates': creates})
def create_detail(request, create_id):
    create = Create.objects.get(id=create_id)
    return render(request, 'create_detail.html', {'create': create})