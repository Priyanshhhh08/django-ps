from django.urls import path
from . import views

urlpatterns = [
    path('emit/', views.emit_signal_in_transaction, name='emit_signal'),
]
