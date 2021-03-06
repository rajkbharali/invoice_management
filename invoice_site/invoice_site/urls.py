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
    path('login/',v.login_page,name='login'),
    path('register/',v.register,name='register'),
    path('dashboard_agent/', v1.dashboard_agent,name='dashboard_agent'),
    path('dashboard_manager/', v1.dashboard_manager,name='dashboard_manager'),
    path('dashboard_agent/details/',v1.dashboard_agent_details,name='details'),
    path('dashboard_agent/details/<user_id>/',v1.dashboard_agent_item_details,name='item_details'),
    path('end/',v1.end_page,name='end_page'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
