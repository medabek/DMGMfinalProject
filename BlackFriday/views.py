from django.shortcuts import render, redirect
from rest_framework import generics

from BlackFriday.serializers import PersonSerializer
from .forms import HomeForm
from .models import Person
from .dataTest import Data
from django.contrib import messages
from ww import f

def home_view(request):
    next = request.GET.get('next')
    form = HomeForm(request.POST or None)
    if form.is_valid():
        gender = form.cleaned_data.get('gender')
        age = form.cleaned_data.get('age')
        occupation = form.cleaned_data.get('occupation')
        city_category = form.cleaned_data.get('city_category')
        stay_years = form.cleaned_data.get('stay_years')
        #marital = form.cleaned_data.get('marital')
        product_id = form.cleaned_data.get('product_id')
        purchase = form.cleaned_data.get('purchase')
        messages.success(request, f('Valid inputs, good job!'))
        h = Person(gender=gender, age=age, occupation=occupation, city_category=city_category, stay_years=stay_years,  product_id=product_id, purchase=purchase)
        a = []
        a.append(h.gender)
        a.append(h.age)
        a.append(h.occupation)
        a.append(h.city_category)
        a.append(h.stay_years)
        #a.append(h.marital)
        a.append(h.product_id)
        a.append(h.purchase)

        e = []
        e.append(a)
        print(e)

        d = Data.data_min(e)
        prediction = int(d[0])
        print(type(d))
        h.save()
        if(prediction==1):
            messages.info(request, f('The Prediction is MARRIED'))
        elif(prediction==0):
            messages.info(request, f('The Prediction is NOT MARRIED'))
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'home_form.html', context)

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.filter(id=1)
    serializer_class = PersonSerializer

class PersonView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
