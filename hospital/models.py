from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	rt = [
		(0,'Guest'),
		(1,'Doctor'),
		(2,'Patient'),
		
		
	]
	eid = models.CharField(max_length=20)
	role_type = models.IntegerField(default=0)

	
class PatientProfile(models.Model):
	pgr = [
	      ("h","select your Gender"),
	    ('M',"Male"),
	    ('F',"Female"),
	]
	ptage = models.IntegerField()
	pmobile = models.IntegerField()
	pweigth = models.IntegerField()
	pgr = models.CharField(max_length=5,default='h',choices=pgr)
	pstatus = models.BooleanField(default=0)
	ptd = models.OneToOneField(User,on_delete=models.CASCADE)

class DoctorProfile(models.Model):
	patients = models.ManyToManyField(PatientProfile, related_name='doctors')
	g = [
	    ("k","select your Gender"),
	    ('M',"Male"),
	    ('F',"Female"), 
	]
	s = [
	    ('G','----Select Specialites----'),
	    ('General Medicine','General Medicine'),
	    ('Urology & Andrology','Urology & Andrology'),
	    ('Neurology','Neurology'),
		('Orthopaedics','Orthopaedics'),
		('Cardiology','Cardiology'),
		('Stomach','Stomach'),
		('ENT','ENT'),
	]
	dage = models.IntegerField()
	dmobile = models.IntegerField()
	dgr = models.CharField(max_length=50,default='k',choices=g)
	dspecialites = models.CharField(max_length=50,default='G',choices=s)
	dexpr = models.IntegerField()
	ddesg = models.CharField(max_length=10)
	dstatus = models.BooleanField(default=0)
	dch = models.OneToOneField(User,on_delete=models.CASCADE)






	


class Problem(models.Model):

	patient_by = models.ForeignKey(User, on_delete=models.CASCADE)
	p_list = [
		('P' , 'select your problem'),
		('Orthopaedics','leg and Hand pain'),
		('Orthopaedics','neck and Back pain'),
		('Cardiology','chest pain'),
		('Neurology','head pain'),
		('Stomach','stomach pain'),
		('ENT','cough and cold and ear'),
		('General Medicine','others')

	]
	p_status = [
		('Success','Success'),
		('Pending','Pending')
	]
	prob = models.CharField(default='P',choices=p_list,max_length=50)
	desc_of_problem = models.TextField()
	date_of_occurrence = models.DateField()
	req_date = models.DateField(auto_now=True)
	problem_status = models.CharField(default='Pending',choices=p_status,max_length=50)


class ProblemSolution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    solution_text = models.TextField()
    solution_date = models.DateField(auto_now=True)















