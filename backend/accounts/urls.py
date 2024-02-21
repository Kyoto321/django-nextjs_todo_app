from django.urls import path, re_path
from .views import (
    SignUpView,
    CustomProviderAuthView,
    LogoutView
)

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('signup/', SignUpView.as_view()),
    path('logout/', LogoutView.as_view()),
]