from django.shortcuts import render
from .models import Tweeter
from .forms import TweeterForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request ,'index.html')

def tweeter_list(request):
  tweets = Tweeter.objects.all().order_by('-created_at')
  return render(request,'tweeter_list.html',{'tweets':tweets})

@login_required
def tweeter_create(request):
   if request.method == "POST":
    form = TweeterForm(request.POST,request.FILES)
    if form.is_valid():
       tweet=form.save(commit=False)
       tweet.user=request.user
       tweet.save()
       return redirect('tweeter_list')
   else:
      form=TweeterForm()
   return render(request,'tweeter_form.html',{'form':form})

@login_required
def tweeter_edit(request,tweet_id):
   tweet=get_object_or_404(Tweeter,pk=tweet_id,user=request.user)
   if request.method == 'POST':
    form = TweeterForm(request.POST,request.FILES,instance=tweet)
    if form.is_valid():
       tweet=form.save(commit=False)
       tweet.user=request.user
       tweet.save()
       return redirect('tweeter_list')
   else:
      form=TweeterForm(instance=tweet)
   return render(request,'tweeter_form.html',{'form':form})

@login_required
def tweeter_delete(request,tweet_id):
  tweet = get_object_or_404(Tweeter,pk=tweet_id,user=request.user)
  if request.method == 'POST':
   tweet.delete()
   return redirect('tweeter_list')
  return render(request,'tweeter_confirm_delete.html',{'tweet':tweet})

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user=form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request,user)
      return redirect('tweeter_list')
  else:
    form=UserRegistrationForm()
  return render(request,'registration/register.html',{'form':form})
  
