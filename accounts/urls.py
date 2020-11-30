from django.urls import path
import accounts.views

urlpatterns = [
 path('', accounts.views.logout, name='logout'),

]
