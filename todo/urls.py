from django.urls import path,
from .views import TodoAPIView

urlpatterns = [
    path('', TodoAView.as_view(), name='todo-list'),
]