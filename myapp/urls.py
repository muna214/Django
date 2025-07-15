from django.urls import path
from .views import ApiRoot, StudentListAPI, RegisterAPI, LoginView

urlpatterns = [
    path('api/', ApiRoot.as_view(), name='api-root'),   # ✅ add this
    path('api/students/', StudentListAPI.as_view(), name='student-list'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]
