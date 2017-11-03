"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from mysite import settings
from mysite import views as sv  # site views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^store/', include('ecommerce.urls')),
    url(r'^$', sv.index),
    url(r'^contact/$', sv.contact),
    url(r'^faq/$', sv.faq),
    url(r'^team/$', sv.team),
    url(r'^features/$', sv.features),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
