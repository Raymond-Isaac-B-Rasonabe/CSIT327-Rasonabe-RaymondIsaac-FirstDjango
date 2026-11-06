from django.urls import path
from .views import DashboardView, AdminPanelView
urlpatterns = [
    path("view/", DashboardView.as_view(), name="dashboard"),
    path("admin-panel/", AdminPanelView.as_view(), name="admin_panel"),
]
