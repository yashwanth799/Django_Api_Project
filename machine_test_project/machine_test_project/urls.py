"""
URL configuration for machine_test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from applciation import views


urlpatterns = [
    path('add_Clients/<id>/', views.add_clients),
    path("AllClients/", views.ClientApiView.as_view()),

    path("Client_id/<int:id>/", views.ClientView.as_view()),
    path("Client_id_update/<int:id>/", views.ClientViewUpdate.as_view()),
    path("Client_id_delete/<int:id>/", views.ClientViewDelete.as_view()),

    # path("Client_id_project/", views.ProjectView.as_view()),

    path('projects/', views.ProjectView.as_view()),

    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path(' ', include('applciation.urls')),
]
