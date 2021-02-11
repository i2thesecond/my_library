from .views import bookAPIView
from django.conf.urls import url
app_name = 'server'
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]

