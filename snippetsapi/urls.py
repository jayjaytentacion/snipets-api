from django.urls import path
from snippetsapi import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(),name='snippets'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippets_detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]