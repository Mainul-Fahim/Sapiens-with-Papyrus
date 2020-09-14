
from django.urls import path
from .views import  BookCheckoutView, paymentComplete


urlpatterns = [
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    ]