from django.urls import path, re_path, include
from .views import (
    SignUpView,
    CustomProviderAuthView,
    RetrieveUserView,
    LogoutView
)

urlpatterns = [
    #re_path(r'^o/(?P<provider>\S+)/$', CustomProviderAuthView.as_view(), name='provider-auth'),
    path('signup/', SignUpView.as_view()),
    #path('github/', GitHubLogin.as_view(), name='github_login'),
    path('user/', RetrieveUserView.as_view()),
    path('social-auth/', include('social_django.urls', namespace='social-auth')),
    path('logout/', LogoutView.as_view()),
]

