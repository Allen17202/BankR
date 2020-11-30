from django.urls import path
import transactionrecord.views

urlpatterns = [
 path('', transactionrecord.views.record, name='record'),
]
