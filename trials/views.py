import csv, io
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from trials.forms import UserForm, UserProfileInfoForm, searchForm, trialForm, selectedTrialForm, searchForm1, updateForm
from trials.models import cancerTypes, trial, bodyRegion, trial_lead
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

def index(request):    
    # check if they have submitted a search
    if request.method == "POST":       
        search_form = searchForm(data=request.POST)               
        if search_form.is_valid():
            # need to check for matches in the database
            if search_form.cleaned_data["Trial_ended"] == False:                
                # todays date variable to only return trials that havent ended
                now = datetime.datetime.now()
                returned_trials = trial.objects.filter(
                    Q(body_region__exact=search_form.cleaned_data["body_region"]) & 
                    # Q(cancer_type__exact=search_form.cleaned_data["cancer_type"]) &
                    Q(end_date__gt = now)).values()                                    
                return render(request,'trials/searchresults.html',
                                {'trials':returned_trials
                                })
            else:
                returned_trials = trial.objects.filter(
                    Q(body_region__exact=search_form.cleaned_data["body_region"]))                      
                return render(request,'trials/searchresults.html',
                                {'trials':returned_trials
                                })
        else:
            #if form not valid print out errors to terminal update for prod app
            print(search_form.errors)
            return render(request,"trials/error.html",{
            "msg": "form not valid"
            }) 
            
    else:
        # view for dependent cancer typ drop down box only
        search_form = searchForm1()
        return render(request,'trials/index.html',
                                {'search_form':search_form
                                })

@login_required
def user_logout(request):
    logout(request)    
    return HttpResponseRedirect(reverse('trials:index'))

#Create View - decorator so needs to be logged in
@login_required
def addtrial(request):
    # check if form is being requested or has been completed. 
    if request.method == "POST":
        trial_form = trialForm(data=request.POST)
        #checks submitted form is valid and if is saves to database
        if trial_form.is_valid():
            trial_form.save()
            return HttpResponseRedirect(reverse('trials:index'))
        else:
            #if form not valid print out errors to terminal update for prod app
            print(trial_form.errors)
    # if first vist return form
    else:
        trial_form = trialForm()
        return render(request, 'trials/addtrial.html',
                                {'trial_form':trial_form
                                })

def register(request):
    # used to check if user is registered
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()
            # add additional information phone number
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True            
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'trials/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered': registered})

def user_login(request):
    # need to update so it doesn't errorif the wrong details are entered
    if request.method == 'POST':
        # username and password in bracket relates to 'names' username and password specified in login.html
        username = request.POST.get('username')
        password = request.POST.get('password')

        # user Django builting authentication method
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('trials:index'))
            else:
                return HttpResponse("Account not activer")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password {password}")
            return HttpResponse("Invalid Logn Details")
    else:
        return render(request, 'trials/login.html')

# Read View
def get_trial(request,id):
    '''
        Get page for selected trial
        1. get full trial deails        2. 
        3. if content not found, redirect to error page
    '''    
    try:
        trialSelected = trial.objects.get(id=id)
    except:
        return redirect('trials:index') 
    
       
    if trialSelected is None:
    # no trial found 
        return render(request,"trials/error.html",{
            "msg": "no trial of that name"
        }) 
    else:        
    # trial found
    # issue with end date due to form how do we get drop down but over write when completed?
    # to access trialSelected.trial_lead is foreign key other firld in foreign modle access by.field names
    #e.g. trialSelected.trial_lead.email and trialSelected.trial_lead.contact below
        data = {
            'name': trialSelected.name,
            'description': trialSelected.description,
            'end_date': trialSelected.end_date,
            'inclusion_criteria': trialSelected.inclusion_criteria,
            'exclusion_criteria': trialSelected.exclusion_criteria,
            'body_region': trialSelected.body_region,
            'cancer_type': trialSelected.cancer_type,
            'trial_lead': trialSelected.trial_lead,
            'email': trialSelected.trial_lead.email,
            'contact': trialSelected.trial_lead.contact
        }
        trial_form = selectedTrialForm(initial=data)           
    
        return render(request,"trials/trialpage.html",{                
                "trial_form":trial_form,
                "trialSelected":trialSelected       
            })

def load_cancer_type(request):
    body_region = request.GET.get('body_region')
    cancer_type = cancerTypes.objects.filter(body_region=body_region).order_by('cancer_type') 
    return render(request, 'trials/cancer_dropdown_list_options.html', {'cancer_type': cancer_type})

# Update View - decorator so needs to be logged in
@login_required
def trial_update(request, id):    
    if request.method == 'POST':
        # need to get the trial to update rather than create
        selected = trial.objects.get(id=id)
        # creates an the update of the instance called.
        update_form = updateForm(request.POST, instance=selected)
        if update_form.is_valid():            
            update_form.save() 
            # search form to create new index page when redirected.
            search_form = searchForm1()          
            return render(request,'trials/index.html',
                                {'search_form':search_form,
                                 "msg": "Trial Saved"
                                })           
        else:
            return render(request,"trials/error.html",{
            "msg": update_form.errors
            })
    else:
        return redirect('index')

@login_required
def csv_upload(request):
    template = "trials/trial_upload.html"
    prompt = {
        'order': 'Order of CSV should be name, description, end_date (YYYY-MM-DD), inclusion_criteria, exclusion_criteria, body_region, cancer_type, trial_lead, use "" to enclose fields containing commas'
    }

    if request.method == "POST":
        csv_file = request.FILES['file']
        # check the file is a CSV
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a csv File')
        else:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            # skip first line as usually a header
            next(io_string)
            # print(f'the io_string: {io_string.read()}')            
            for column in csv.reader(io_string, delimiter=',', quotechar='"'):
                _, created = trial.objects.update_or_create(
                    name=column[0],
                    description=column[1],
                    end_date=column[2], 
                    inclusion_criteria=column[3], 
                    exclusion_criteria=column[4], 
                    body_region=bodyRegion.objects.get(body_region = column[5]), 
                    cancer_type=cancerTypes.objects.get(cancer_type = column[6]), 
                    trial_lead=trial_lead.objects.get(last_name = column[7]),                    
                )
        context = {}
        return render(request,template, context)
    else:
        return render(request, template, prompt)
