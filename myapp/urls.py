from django.urls import path
from.import views
urlpatterns = [
    path('loginform/', views.loginform, name='loginform'),
    path('signup/', views.signup, name='signup'),
    path('registration/', views.registration, name='registration'),
    path('showdetails/', views.showdetails, name='showdetails'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
