from django.shortcuts import render
from django.http import HttpResponse
from .models import Child, Fees
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime, timedelta



def home(request):
    return render(request, 'base/home.html')

@login_required
def viewChildred(request):
    context = {
        'children': Child.objects.all(),
        'fees' : Fees.objects.all()
    }

    return render(request, 'base/children.html', context)


@login_required
def pendingFees(request):

    curr_time = datetime.now()
    prev_month = curr_time - timedelta(days=curr_time.today().day)
    curr_month_str = curr_time.strftime("%B").lower()
    prev_month_str = prev_month.strftime("%B").lower()

    safe = [curr_month_str, prev_month_str]

    child_fees_given = set(list(Fees.objects.filter(month__in = safe).values_list('child_id', flat=True)))

    all_childs = set(list(Child.objects.all().values_list('id', flat=True)))

    not_given_fees = list(child_fees_given ^ all_childs)


    childs_no_fees = Child.objects.filter(id__in = not_given_fees, enrolled = True)

    context = {
        'children': childs_no_fees
    }

    return render(request, 'base/pendingFees.html', context)


@login_required
def childFees(request, pk):

    child_fees = Fees.objects.filter(child_id = pk)

    try:
        latest = child_fees.order_by('-date')[0]
    except:
        latest = 1


    if latest == 1:
        context = {
        'fees' : Fees.objects.filter(child_id = pk),
        }
    else:
        context = {
        'fees' : Fees.objects.filter(child_id = pk),
        'latest' : latest
        }
    

    return render(request, 'base/childFees.html', context)


class allFees(LoginRequiredMixin, ListView):
    model = Fees
    template_name = 'base/allFees.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'fees'
    ordering = ['-date']

class FeesCreateView(LoginRequiredMixin, CreateView):
    model = Fees
    fields = ['child', 'month', 'amount', 'date']

    def form_valid(self, form):
        return super().form_valid(form)