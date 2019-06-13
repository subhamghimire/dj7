from django.urls import path
from regapp import views
#template url
app_name = 'regapp'

urlpatterns=[
    path('register/',views.register,name='register'),
]
