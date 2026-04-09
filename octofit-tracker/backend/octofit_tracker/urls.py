"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse

# Codespace-aware base URL (for documentation/future use)
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


# Placeholder API root with codespace-aware URL
def api_root(request):
    return JsonResponse({
        "message": "OctoFit API root",
        "api_base_url": base_url + "/api/"
    })

# Root redirect to API
from django.shortcuts import redirect
def root_redirect(request):
    return redirect('api-root')

router = routers.DefaultRouter()

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
