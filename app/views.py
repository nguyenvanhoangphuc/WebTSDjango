from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
# from .models import Account
from .models import *
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# import json
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TraSua

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
                return render(request, 'app\TrasuaList.html')
            if (account.roles == 'AD'):
                # Lấy danh sách đơn hàng
                context = { 'listDH': DonHang.objects.all() }
                print(context)
                return render(request, 'app\DonhangList.html', context)
    else:
        return render(request, 'app\Login.html', {})    
    # Admin a = AuthenticationBO.getAccount(user, pass);
    # if (a!=null) {
    #     if (a.getRoles().equals("KH")) {
    #         request.getSession().setAttribute("account", a);
    #         request.getRequestDispatcher("Trasua").forward(request, response);
    #     }
    #     if (a.getRoles().equals("AD")) {
    #         request.getSession().setAttribute("account", a);
    #         request.getRequestDispatcher("Donhang").forward(request, response);
    #     }
    # }
    # else {
    #     request.getRequestDispatcher("LoginFail.jsp").forward(request, response);
    # }

class TraSuaList(ListView):
    model = TraSua
    context_object_name = 'trasuas'
    template_name = 'app/TrasuaList.html'

class TraSuaDetail(DetailView):
    model = TraSua
    context_object_name = 'trasua'
    template_name = 'app/TrasuaDetail.html'
