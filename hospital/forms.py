from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","eid","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"eid" : forms.TextInput(attrs={
			"class" : "form-control my-2",
			"placeholder" : "Enter your Id"
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Email",
			}),
		}

class Dprofile(forms.ModelForm):
	class Meta:
		model = DoctorProfile
		fields = ['dage','dmobile','dgr','dspecialites','dexpr','ddesg']
		widgets = {
			"dage" : forms.NumberInput(attrs={
				"class" : 'form-control my-2',
				"placeholder" : 'Enter age'
				}),
			"dmobile" : forms.TextInput(attrs={
				"class" : 'form-control my-2',
				"placeholder" : 'Enter mobile',
				}),
				'dgr' : forms.Select(attrs={
					"class" : 'form-control my-2',
				    "placeholder" : 'select gender',
				}),
				'dspecialites' : forms.Select(attrs={
					"class" : 'form-control my-2',
				    "placeholder" : 'Select Specialites',
				}),

				'dexpr' : forms.NumberInput(attrs={
				"class" : 'form-control my-2',
				"placeholder" : 'Enter experince'
				}),
				'ddesg' : forms.TextInput(attrs={
				"class" : 'form-control my-2',
				"placeholder" : 'designation',
				}),
		}

class PForm(forms.ModelForm):
	class Meta:
		model = PatientProfile
		fields = ['ptage','pmobile','pweigth','pgr']
		widgets = {
			'ptage' : forms.NumberInput(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter age'

			}),
			'pmobile' : forms.NumberInput(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter number'

			}),
			'pweigth' : forms.NumberInput(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter weight'

			}),
			'pgr' : forms.Select(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter gender'

			}),

		}
class ProblemForm(forms.ModelForm):
	
	class Meta:
		model = Problem
		fields = ['prob','desc_of_problem','date_of_occurrence']
		widgets = {
			'prob' : forms.Select(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Select your problem'
			}),
			'desc_of_problem' : forms.Textarea(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'desc of problem',
				'rows' : 4,

			}),
			'date_of_occurrence' : forms.TextInput(attrs={
				'class' : 'form-control my-2',
				"type":"date",
				
			})

		}

class SolutionForm(forms.ModelForm):
	
	class Meta:
		model = ProblemSolution 
		fields = ['solution_text']
		widgets = {
			'solution_text' : forms.Textarea(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter solution',
				'rows' : 4,

			}),
		}

	
