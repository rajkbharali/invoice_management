"""invoice_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views as v
from invoice_app import views as v1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('accounts.urls',namespace='accounts')),
    path('',include('django.contrib.auth.urls')),
    # path('', include('invoice_app.urls', namespace='invoice_app')),
    path('register/',v.register,name='register'),
    path('dashboard/', v1.dashboard,name='dashboard'),
    path('dashboard/details/',v1.DetailsPage.as_view(),name='details'),
    # path('login/',v.login,name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)