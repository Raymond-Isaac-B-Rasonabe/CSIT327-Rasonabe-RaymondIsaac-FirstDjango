from django.urls import path
from .views import CustomUserUpdateView, SignUpView
urlpatterns = [
    path("signup/", SignUpView.as_view(),
        name="signup"),
    
    path("update/", CustomUserUpdateView.as_view(),
            name="update_user"),
]
