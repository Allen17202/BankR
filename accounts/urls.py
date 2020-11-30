from django.urls import path
import accounts.views

urlpatterns = [
 path('logout/', accounts.views.logout, name='logout'),
]
