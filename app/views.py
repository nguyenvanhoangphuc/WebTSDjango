from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
# from .models import Account
from .models import *
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# import json
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import TraSua
from .models import DonHang

# Create your views here.
def login(request):
    return render(request, 'app\Login.html')
    
def view_check_login(request): 
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = Account.objects.get(username=username, password= password)
        print(account,"-----------------------------------------------------------------")
        # print("count", len(account))
        if (account is not None): 
            serialized_account = {'username': account.username, 'password': account.password, 'roles': account.roles}
            request.session['account'] = serialized_account
            if (account.roles == 'KH'):
                # chuyển đển url tra_sua_list
                return redirect('tra_sua_list')
                # return render(request, 'app\TrasuaList.html')
            if (account.roles == 'AD'):
                # chuyển đến url don_hang_list
                return redirect('don_hang_list')
    else:
        return render(request, 'app\Login.html', {})    
def logout(request):
    if 'account' in request.session:
        del request.session['account']
    return redirect('login')

class TraSuaList(ListView):
    model = TraSua
    context_object_name = 'trasuas'
    template_name = 'app/TrasuaList.html'

class TraSuaDetail(DetailView):
    model = TraSua
    context_object_name = 'trasua'
    template_name = 'app/TrasuaDetail.html'

def them_don_hang(request, tra_sua_id):
    if 'account' in request.session:
        username = request.session.get('account').get('username')
    DonHang.objects.create(idts_id=tra_sua_id, username_id = username, isdeliver = False)
    return render(request, 'app\DathangThanhCong.html')

class TraSuaCreate(CreateView):
    model = TraSua
    fields = '__all__'
    success_url = reverse_lazy('tra_sua_list')
    template_name = 'app/TrasuaCreate.html'
    context_object_name = 'trasuacreate'
    
def them_tra_sua (request):
    if request.method == 'GET':
        return render(request, 'app\TrasuaCreate.html')
    else: 
        title = request.POST.get('title')
        price = request.POST.get('price')
        size = request.POST.get('size')
        TraSua.objects.create(title=title, price=price, size=size)
        return redirect('tra_sua_list')
        

class TraSuaUpdate(UpdateView):
    model = TraSua
    fields = '__all__'
    template_name = 'app/TrasuaCreate.html'
    success_url = reverse_lazy('tra_sua_list')
    context_object_name = 'trasuaupdate'
    
def cap_nhat_tra_sua(request, tra_sua_id=''):
    if request.method == 'GET': 
        context = { 'trasua': TraSua.objects.get(id=tra_sua_id) }
        return render(request, 'app\TrasuaUpdate.html', context)
    else: 
        trasua = TraSua.objects.get(id=request.POST.get('oldIDTS')) 
        trasua.title = request.POST.get('title')
        trasua.price = request.POST.get('price')
        trasua.size = request.POST.get('size')
        trasua.save()
        return redirect('tra_sua_list')

class TraSuaDelete(DeleteView):
    model = TraSua
    context_object_name = 'trasua'
    success_url = reverse_lazy('tra_sua_list')
    template_name = 'app/TrasuaDelete.html'
    
def mua_all_tra_sua(request): 
    if 'account' in request.session:
        username = request.session.get('account').get('username')
    if request.method == 'POST':
        list_tra_sua = TraSua.objects.all()
        print(request.POST)
        for tra_sua in list_tra_sua:
            if (str(tra_sua.id) in request.POST.keys()):
                DonHang.objects.create(idts_id=tra_sua.id, username_id = username, isdeliver = False)
    return render(request, 'app\DathangThanhCong.html')


def don_hang_list(request):  
    context = { 'listDH': DonHang.objects.all() }
    return render(request, 'app\DonhangList.html', context)

def cap_nhat_don_hang(request, don_hang_id):
    don_hang = get_object_or_404(DonHang, id=don_hang_id)
    don_hang.isdeliver = not don_hang.isdeliver
    don_hang.save()
    print(request.method)
    return redirect('don_hang_list')

def xoa_don_hang(request, don_hang_id): 
    don_hang = get_object_or_404(DonHang, id=don_hang_id)
    don_hang.delete()
    return redirect('don_hang_list')

def xoa_all_don_hang(request): 
    if request.method == 'POST':
        list_don_hang = DonHang.objects.all()
        print(request.POST)
        for don_hang in list_don_hang:
            if (str(don_hang.id) in request.POST.keys()):
                don_hang.delete()
    return redirect('don_hang_list')