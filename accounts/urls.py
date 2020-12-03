from django.urls import path
import accounts.views

urlpatterns = [
 path('', accounts.views.logout, name='logout'),
 path('transfer/', accounts.views.transfer, name='transfer'),
 path('record/', accounts.views.record, name='record'),
]
