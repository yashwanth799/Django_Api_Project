from django.urls import path
from . import views


urlpatterns = [

    path('add-client/', views.add_client, name='add_client'),
    path('add-project/', views.add_project, name='add_project'),
    path('edit-client/<int:pk>/', views.edit_client, name='edit_client'),
    path('delete-client/<int:pk>/', views.delete_client, name='delete_client'),
    path('clients/', views.client_list, name='client_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('project_list/', views.project_list, name='project_list'),

    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),

    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),

    # path('add_Clients/<id>/', views.add_clients),


]
