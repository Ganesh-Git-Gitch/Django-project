
from django.urls import path
from hospital import views
from django.contrib.auth import views as ad

urlpatterns = [

    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.SignupPage,name='register'),
    path('login/',ad.LoginView.as_view(template_name='login.html'),name="login"),
    path('lgot/',ad.LogoutView.as_view(template_name='logout.html'),name="lgot"),
    path('pfe/', views.profile,name="pf"),
    
    path('upf/',views.updpf,name="upfe"),
    path('create-problem/', views.create_problem, name='create_problem'),
    path('edit-problem/<int:problem_id>/', views.edit_problem, name='edit_problem'),
    path('delete-problem/<int:problem_id>/', views.delete_problem, name='delete_problem'),

    path('docview/',views.docview,name='docview'),
    path('view_problem/<int:problem_id>/', views.view_problem_details, name='view_problem_details'),
    path('docdashboard/', views.docdashboard, name='docdashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    
    path('edit_solution/<int:solution_id>/', views.edit_solution, name='edit_solution'),

    



]
