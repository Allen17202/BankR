from django.urls import path
import transferfunds.views

urlpatterns = [
 path('', transferfunds.views.transferMoney, name='transferMoney'),
]
