from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from common.models import Item, Bidding
from vendor.models import Vendor
# Create your views here.

def index(request):
    return render(request, 'common/index.html')

@csrf_exempt
def signIn(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])
        # authenticate user
        if user is not None:
            try:
                print(Vendor.objects.get(user_id=user.id))
                # Match password
                if check_password(request.POST['password'],user.password):
                    auth.login(request,user)
                    return redirect('common:dashboard')
                else:
                    return HttpResponse("Wrong password")
            except:
                return HttpResponse("Not vendor")
        else:
            return HttpResponse("Invalid (check email/password)")
    return render(request,'common/signin.html')


@login_required(login_url='common:signIn')
def dashboard(request):
    '''
    If login as user then user:dashboard
    else
    vendor:dashboard
    '''
    context = {}
    items = Item.objects.all()
    for item in items:
        try:
            item.price_bid = Bidding.objects.get(user_id=request.user.id, item_id=item.id).bidding_amount
        except:
            item.price_bid = False
    
    context['items'] = items
    return render(request, 'common/items.html', context)


@login_required(login_url='common:signIn')
def logout(request):
    auth.logout(request)
    return redirect('common:signIn')


def bidNow(request,item_id):
    # Fetch item
    item = Item.objects.get(pk=item_id)
    context = {'item':item}
    return render(request, 'common/bid.html', context)

def saveBid(request):
    if request.method == 'GET':
        item_id = int(request.GET['item_id'])
        bid_price = float(request.GET['bid_price2'])
        # save in bidding table
        bidding = Bidding()
        bidding.user_id = int(request.user.id)
        bidding.item_id = item_id
        bidding.bidding_amount = bid_price
        bidding.save()
        return redirect('common:dashboard')
    else:
        return HttpResponse("Not working")

