from django.urls import path, include
from rest_framework import routers

from api.views import tag, post, comment
from user.views import profile

