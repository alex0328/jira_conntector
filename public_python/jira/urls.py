from django.urls import path, re_path
from jira import views

app_name = 'jira'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    ]