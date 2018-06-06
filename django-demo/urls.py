"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from quotes.views import Register
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/success/$',
        TemplateView.as_view(template_name="registration/success.html"),
        name='register-success'),
    url(r'^register/$',
        Register.as_view(),
        name='register'),
    url(r'^quote', include('quotes.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]