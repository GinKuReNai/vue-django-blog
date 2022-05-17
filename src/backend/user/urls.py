from django.urls import path
from user.views import profile

app_name = 'profile'

urlpatterns = [
  path('', profile.ProfileListAPIView.as_view(), name='list_profile'),
  path('create/', profile.ProfileCreateAPIView.as_view(), name='create_profile'),
  path('<uuid:id>/', profile.ProfileDetailAPIView.as_view(), name='detail_profile'),
]