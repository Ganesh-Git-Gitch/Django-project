from django.shortcuts import render,redirect , get_object_or_404
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *
from django.db.models import Q
from django.core.mail import send_mail
from hospital_mgmt import settings
# Create your views here.

def About(request):
	return render(request, 'about.html')

def Home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def SignupPage(request):
    if request.method=='POST':
            usform = UsForm(request.POST)
            if usform.is_valid():
                h = usform.save(commit=False)
                messages.success(request,f"{request.user.username} User created successfully")
                h.save()
                # Send a confirmation email to the registered user
                subject = 'Welcome to Your Website'
                message = 'Thank you for registering on Your Website! Hospital Management System'
                from_email = settings.EMAIL_HOST_USER 
                recipient_list = [h.email]  # Use the user's email address

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                return redirect('/login')
            
    usform = UsForm()    
    return render(request,'signup.html',{'UsForm' : usform})

@login_required
def profile(request):
	return render(request,'profile.html')


@login_required
#doctor

@login_required
def updpf(request):
    if request.method == 'POST':
        if request.user.role_type == 1:  # Doctor profile update
            if hasattr(request.user, 'doctorprofile'):
                form = Dprofile(request.POST, instance=request.user.doctorprofile)
            else:
                form = Dprofile(request.POST)
        elif request.user.role_type == 2:  # Patient profile update
            if hasattr(request.user, 'patientprofile'):
                form = PForm(request.POST, instance=request.user.patientprofile)
            else:
                form = PForm(request.POST)
        else:
            messages.error(request, "Invalid role type")

        if form.is_valid():
            profile = form.save(commit=False)
            if request.user.role_type == 1:
                profile.dch = request.user
                profile.dsatus = 1
            elif request.user.role_type == 2:
                profile.ptd = request.user
                profile.pstatus = 1
            profile.save()
            return redirect('/pfe')
            
    else:
        # GET request, initialize the forms with existing data or empty forms
        if request.user.role_type == 1:
            if hasattr(request.user, 'doctorprofile'):
                form = Dprofile(instance=request.user.doctorprofile)
            else:
                form = Dprofile()
        elif request.user.role_type == 2:
            if hasattr(request.user, 'patientprofile'):
                form = PForm(instance=request.user.patientprofile)
            else:
                form = PForm()
        else:
            messages.error(request, "Invalid role type")

    return render(request, 'updateprofile.html', {'form': form})

@login_required
def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.patient_by = request.user  # Set the patient as the user
            problem.save()

            # Find doctors with the same specialty as the problem and assign them as the patient's doctors
            patient_profile = PatientProfile.objects.get(ptd=request.user)
            matching_doctors = DoctorProfile.objects.filter(dspecialites=problem.prob)
            patient_profile.doctors.set(matching_doctors)
            patient_profile.save()

            return redirect('/create-problem')
   
    form = ProblemForm()

    problems = Problem.objects.filter(patient_by = request.user)
    return render(request, 'create_problem.html', {'form': form, 'problist': problems})

def edit_problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST' :
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('/create-problem')
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'edit_problem.html', {'form': form, 'problem': problem})

def delete_problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        problem.delete()
        return redirect('/create-problem')
    return render(request, 'delete_problem.html', {'problem': problem})



def docview(request):
    if request.user.role_type == 1 and hasattr(request.user, 'doctorprofile'):
        doctor_profile = request.user.doctorprofile
        specialty = doctor_profile.dspecialites

        # Filter problem requests for the doctor's specialty
        problem_requests = Problem.objects.filter(
            Q(prob=specialty) & ~Q(patient_by=request.user) & Q(problem_status = 'Pending')
        )

        return render(request, 'docview.html', {'prob': problem_requests})
    




def view_problem_details(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    patient_profile = problem.patient_by.patientprofile
   
    if request.method == 'POST':
        sol = SolutionForm(request.POST)
        if sol.is_valid():
            solution = sol.save(commit=False)
            solution.problem = problem
            solution.doctor = request.user.doctorprofile  # Assuming the user is a doctor
            problem.problem_status = 'Success'
            problem.save()
            solution.save()
            
            return redirect('/docview')  
         
        
    sol = SolutionForm()
    return render(request, 'patient_details.html',  {'problem': problem, 'patient_profile': patient_profile,'solutionform' : sol})


def docdashboard(request):
    # Query all successful problem solutions

    successful_solutions = ProblemSolution.objects.filter(problem__problem_status='Success')

    return render(request, 'docdashboard.html', {'solutions': successful_solutions})



def patient_dashboard(request):
    if request.user.role_type == 2 and hasattr(request.user, 'patientprofile'):
        patient_profile = request.user.patientprofile

        # Get all problems and their solutions for the patient
        problem_solutions = ProblemSolution.objects.filter(problem__patient_by=request.user)

        return render(request, 'patient_dashboard.html', {'patient_profile': patient_profile, 'problem_solutions': problem_solutions})




def edit_solution(request, solution_id):
    solution = get_object_or_404(ProblemSolution, pk=solution_id)

    if request.method == 'POST':
        form = SolutionForm(request.POST, instance=solution)
        if form.is_valid():
            form.save()
            return redirect('/docdashboard')

    else:
        form = SolutionForm(instance=solution)

    return render(request, 'edit_solution.html', {'form': form, 'solution': solution})










