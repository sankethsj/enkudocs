from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_docs, name="list_docs"),
    path("<str:document_id>", views.list_docs, name="list_docs"),
]