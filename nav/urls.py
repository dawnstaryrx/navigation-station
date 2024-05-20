from django.urls import path
from nav import views

urlpatterns = [
    path("", views.index, name="index"),
    path('app/<int:app_id>',views.app_detail, name="app-detail")
    # path('app/<int:pk>', views.AppDetailView.as_view(), name='app-detail'),
]
