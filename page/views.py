from . import forms
from django.contrib.auth.models import User
from django.shortcuts import render
import datetime
from page.models import Task, Profile, Packet
from page.forms import PostForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def initial(request):
    registered = True
    now = datetime.datetime.now()
    us = User.objects.filter(username=request.user)[0]
    name = us.first_name + "  " + us.last_name
    ps = Profile.objects.filter(user_id=us)[0]
    image = ps.img
    packet_lst = Packet.objects.filter(profile_id=ps).order_by('sDate')
    init_dict = {'dtNow': now, 'packets': packet_lst, 'name': name, 'registered': registered, 'img': image}
    return render(request, 'page/index.html', context=init_dict)


@login_required
def add_new_task(request, packet_id):
    registered = True
    now = datetime.datetime.now()
    us = User.objects.filter(username=request.user)[0]
    ps = Profile.objects.filter(user_id=us)[0]
    image = ps.img
    name = us.first_name + "  " + us.last_name
    packet_lst = Packet.objects.filter(profile_id=ps).order_by('sDate')
    task_lst = Task.objects.filter(box_id=packet_id)
    form = PostForm()
    p = Packet.objects.filter(id=packet_id)[0]
    if str(p.profile_id) != str(us):
        return HttpResponseRedirect(reverse('page:initial'))
    rel_dt = p.sDate
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():

            t = Task(box_id=p, title=form.cleaned_data['title'])

            last_task = task_lst.order_by('eTime').first()
            now = datetime.datetime.now().time()
            if last_task is None:
                pass
            else:
                if last_task.eTime is None:
                    last_task.eTime = now
                    last_task.save()
            t.save()
        else:
            print('ERROR POST FORM')

    task_dict = {'tasks': task_lst, 'dtNow': now, 'relDT': rel_dt, 'packets': packet_lst,
                 'name': name, 'form': form, 'registered': registered, 'img': image}

    return render(request, 'page/index.html', context=task_dict)


@login_required
def add_new_packet(request):
    us = User.objects.filter(username=request.user)[0]
    ps = Profile.objects.filter(user_id=us)[0]
    p = Packet()
    p.profile_id = ps
    p.save()
    return HttpResponseRedirect(reverse('page:add_new_task', args=[p.id]))


@login_required
def end_task(request, task_id):
    t = Task.objects.filter(id=task_id)[0]
    t.eTime = datetime.datetime.now().time()
    t.save()
    return HttpResponseRedirect(reverse('page:add_new_task', args=[t.box_id_id]))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('page:initial'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('page:initial'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return render(request, 'login/login.html', {'error': "نام کاربری یا رمز عبور اشتباه است"})
    else:
        return render(request, 'login/login.html', {})


def user_register(request):
    registered = False
    name = None
    now = datetime.datetime.now()
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        image = ""
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            name = user.first_name + "  " + user.last_name

            profile = profile_form.save(commit=False)
            profile.user_id = user

            if 'img' in request.FILES:
                profile.img = request.FILES['img']
                image = profile.img
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

        reg_dict = {'dtNow': now, 'name': name, 'registered': registered, 'img': image}
        return render(request, 'page/index.html', context=reg_dict)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        reg_dict = {'dtNow': now, 'user_form': user_form,
                    'profile_form': profile_form, 'registered': registered}
        return render(request, 'page/register.html', context=reg_dict)


