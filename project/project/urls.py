"""project URL Configuration

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
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import admin
from django.contirb.auth import views as auth_views

from django.contrib.auth.decorators import login_required
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # login,logout
    path('login', auth_views.LoginView.as_view(template_name='login.html',
                                               redirect_authenticated_user=true),
                                               name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # API ドキュメント
    path('docs/', include_docs_urls(title='API', public=False)),

    #  ノートアプリケーションAPI
    path('note/', include('note.urls')),

    # アプリケーションのUI
    path('', ensure_csrf_cookie(login_required(render)),
        kwargs={'tenplate_name': 'index.html'}, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

