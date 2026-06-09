"""
URL configuration for dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from events.forms import LoginForm

urlpatterns = [
  # Main views
  path("", include("events.urls")),

  # Auth views
  path(
    "accounts/login/",
    auth_views.LoginView.as_view(
      authentication_form=LoginForm
    ),
    name="login",
  ),
  path("accounts/", include("django.contrib.auth.urls")),

  # Admin views
  path("admin/", admin.site.urls, name="admin"),
]


# Only serve user-uploaded media in development.
# This is important because if this application was ever used in a production 
# environment and a user uploaded illegal content, CannyByte would be held 
# responsible for serving it on their website.
if settings.DEBUG:
  urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
  )
