from django.urls import path, include
from snippets.views import SnippetList, SnippetDetail, DogList, DogDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('dogs/', DogList.as_view()),
    path('dogs/<int:pk>/', DogDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)