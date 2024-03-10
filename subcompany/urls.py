from rest_framework.urls import path
from subcompany.views import Userclass,companyclass
urlpatterns = [
    path("api/user/",Userclass.as_view()),
    path("api/user/<int:user_id>/",Userclass.as_view()),
    path("api/company/",companyclass.as_view()),
    path("api/user/<int:user_id>/",companyclass.as_view()),
]
