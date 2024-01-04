from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView,TokenBlacklistView

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from .views import *

urlpatterns = [


]