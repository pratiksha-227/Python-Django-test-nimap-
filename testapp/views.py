from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from testapp.models import Company

# Create your views here.
def home_view(request):
    return render(request,'testapp/Company.html')


class CompanyCreate(CreateView):
    model=Company
    fields=('cid','Client','date','user')

class CompanyList(ListView):
    model=Company

class CompanyDetail(DetailView):
        model=Company

class CompanyUpdate(UpdateView):
    model=Company
    fields=('client','date','user')

class CompanyDelete(DeleteView):
    model=Company
    success_url=reverse_lazy('list')
