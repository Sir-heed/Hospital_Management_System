from django.urls import path, include
from .views import add_record_view, home_view, users_details

app_name = 'record'
urlpatterns = [
    path('', home_view, name='home'),
    path('add', add_record_view, name='add_record'),
    path('users', users_details, name='user_details')
]