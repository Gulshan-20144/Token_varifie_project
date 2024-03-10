from rest_framework.urls import path
from accounts.views import ragistrations,loginview
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/ragistration/',ragistrations.as_view()),
    path('api/login/',loginview.as_view(),name="login"),
    path('api/Refresh/',TokenRefreshView.as_view(),name="token_refresh_view"),
    
]
