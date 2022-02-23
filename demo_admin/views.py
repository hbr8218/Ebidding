from curses.ascii import HT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password  
from .models import DemoAdmin
from django.db.models import Min, Max
from common.models import Item, Bidding

# Create your views here.
def signIn(request):
    if request.method == 'POST':
        admin = User.objects.get(email=request.POST['email'])
        # authenticate user
        if admin is not None:
            try:
                DemoAdmin.objects.get(user_id=admin.id)
                # Match password
                if check_password(request.POST['password'],admin.password):
                    auth.login(request,admin)
                    return redirect('demo_admin:dashboard')
                else:
                    return HttpResponse("Wrong password")
            except:
                return HttpResponse("Not admin")
        else:
            return HttpResponse("Invalid (check email/password)")
    return render(request,'demo_admin/signin.html')



@login_required(login_url='demo_admin:signIn')
def dashboard(request):
    context = {}
    items = Item.objects.all()
    context['items'] = items
    return render(request,'demo_admin/items.html', context)

@login_required(login_url='demo_admin:signIn')
def admin_logout(request):
    auth.logout(request)
    return redirect('demo_admin:signIn')

@login_required(login_url='demo_admin:signIn')
def addItem(request):
    return render(request,'demo_admin/add_item.html')

@login_required(login_url='demo_admin:signIn')
def saveItem(request):
    if request.method == 'GET':
        # get form data
        print(request.GET)
        item_name = request.GET['name']
        bid_price = request.GET['bid_price']
        item = Item()
        item.name = item_name
        item.bid_price = float(bid_price)
        print(item.name, item.bid_price)
        item.save()
        print("saved")
        return redirect('demo_admin:dashboard')
    return redirect('demo_admin:addItem')


def viewBiddings(request):
    context = {}
    items = Bidding.objects.values('item_id').annotate(min_bid_amount=Min('bidding_amount'))
    context['items'] = items
    print(items)
    return render(request, 'demo_admin/successful_biddings.html', context)