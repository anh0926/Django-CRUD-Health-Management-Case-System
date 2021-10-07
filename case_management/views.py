from django.shortcuts import render, redirect
# from django.http import Http404
from .forms import PersonForm, ReferralForm
from .models import Person, Referral 
from django.contrib.auth.decorators import login_required


@login_required
def create_person(request):
    if request.method == "POST":       
        person_form = PersonForm(request.POST)                          
        if person_form.is_valid():
            try:
                person_form.save()                            
                return redirect('/people')
            except:
                pass
    else:
        person_form = PersonForm()              
    return render(request, 'create_person.html', {'person_form': person_form})

@login_required
def people(request):
    people = Person.objects.all()    
    return render(request, "people_index.html",{'people':people})

@login_required
def edit_person(request, id):    
    person = Person.objects.get(id=id)
    return render(request,'edit_person.html',{'person':person})

@login_required
def update_person(request,id):
    person = Person.objects.get(id=id) 
    person_form = PersonForm(request.POST, instance = person)
    if person_form.is_valid():
        person_form.save()
        return redirect("/people") 
    return render(request,'edit_person.html',{'person':person})

@login_required
def delete_person(request,id):  
    person = Person.objects.get(id=id)    
    person.delete()
    return redirect("/people")


@login_required
def show_person (request, id):    
    # person = Person.objects.get(id=id)
    referrals = Referral.objects.filter(person__id = id)
    return render(request,'show_person.html',{'referrals':referrals})

# -----------REFERRALS---------------

@login_required
def create_referral(request):   
    if request.method == "POST":             
        referral_form = ReferralForm(request.POST)                          
        if referral_form.is_valid():
            try:
                referral_form.save()                            
                return redirect('/referrals')
            except:
                pass
    else:
        referral_form = ReferralForm()              
    return render(request, 'create_referral.html', {'referral_form': referral_form})

@login_required
def referrals(request):
    referrals = Referral.objects.all()    
    return render(request, "referrals_index.html",{'referrals':referrals})

@login_required
def edit_referral(request, id):    
    referral = Referral.objects.get(id=id)
    return render(request,'edit_referral.html',{'referral':referral})

@login_required
def update_referral(request,id):
    referral = Referral.objects.get(id=id)
    if request.method == "POST":          
        referral_form = ReferralForm(request.POST, instance = referral)
        if referral_form.is_valid():
            referral_form.save()
        return redirect("/referrals") 
    return render(request,'edit_referral.html',{'referral':referral})

@login_required
def delete_referral(request,id):  
    referral = Referral.objects.get(id=id)    
    referral.delete()
    return redirect("/referrals")

@login_required
def show_referral (request, id):    
    referral = Referral.objects.get(id=id)    
    return render(request,'show_referral.html',{'referral':referral})
