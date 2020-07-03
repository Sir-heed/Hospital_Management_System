from django.urls import path, include
from .views import staff_signup_view, login_view, logout_view, patient_signup_view

app_name = 'users'
urlpatterns = [
    path('staff/signup/', staff_signup_view, name='staff_signup'),
    path('user/signup/', patient_signup_view, name='patient_signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]