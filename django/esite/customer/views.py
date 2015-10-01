from django.shortcuts import render_to_response, get_object_or_404

from models import Customer


def get_customers(request):
    customers = Customer.objects.filter(active=True)
  
    return render_to_response('list.html', {
        'page_title': 'Customers',
        'customers': customers,
    })
