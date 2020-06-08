from django.urls import path
from invoice_app import views

app_name = 'invoice_app'

urlpatterns = [
    path('home/',views.HomePage.as_view(),name='home'),
    path('home/details/',views.DetailsPage.as_view(),name='details'),
]