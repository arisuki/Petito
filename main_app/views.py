import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, Photo
from .forms import FeedingForm, CleaningForm, LovingForm, MovingForm, SleepingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # later we need to RE-DIRECT to the INDEX!!!!
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def petitos_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'petitos/index.html', {
        'pets': pets 
    })

@login_required
def petitos_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'petitos/detail.html', {'pet':pet})


class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'species', 'color', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['color', 'bio']

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/petitos'

@login_required
def add_feeding(request, pet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('task_feeding', pet_id = pet_id)

@login_required
def add_cleaning(request, pet_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.pet_id = pet_id
        new_cleaning.save()
    return redirect('task_cleaning', pet_id = pet_id)

@login_required
def add_loving(request, pet_id):
    form = LovingForm(request.POST)
    if form.is_valid():
        new_loving = form.save(commit=False)
        new_loving.pet_id = pet_id
        new_loving.save()
    return redirect('task_loving', pet_id = pet_id)

@login_required
def add_moving(request, pet_id):
    form = MovingForm(request.POST)
    if form.is_valid():
        new_moving = form.save(commit=False)
        new_moving.pet_id = pet_id
        new_moving.save()
    return redirect('task_moving', pet_id = pet_id)

@login_required
def add_sleeping(request, pet_id):
    form = SleepingForm(request.POST)
    if form.is_valid():
        new_sleeping = form.save(commit=False)
        new_sleeping.pet_id = pet_id
        new_sleeping.save()
    return redirect('task_sleeping', pet_id = pet_id)

@login_required
def tasks(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/tasks.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })


@login_required
def task_feeding(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/task_feeding.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })

@login_required
def task_cleaning(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/task_cleaning.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })

@login_required
def task_loving(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/task_loving.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })

@login_required
def task_moving(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/task_moving.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })

@login_required
def task_sleeping(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    feeding_form = FeedingForm()
    cleaning_form = CleaningForm()
    loving_form = LovingForm()
    moving_form = MovingForm()
    sleeping_form = SleepingForm()
    return render(request, 'petitos/task_sleeping.html', {'pet':pet, 'feeding_form': feeding_form, 'cleaning_form': cleaning_form, 'loving_form': loving_form, 'moving_form': moving_form, 'sleeping_form': sleeping_form })

@login_required
def add_photo(request, pet_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to pet_id or pet (if you have a pet object)
            Photo.objects.create(url=url, pet_id=pet_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', pet_id=pet_id)