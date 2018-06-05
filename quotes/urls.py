from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.quote_req, name='quote-request'),
    url(r'show/(?P<pk>[0-9]+)$',
        views.QuoteView.as_view(), name='quote-detail'),
    url(r'show$',
        views.QuoteList.as_view(), name='show-quotes'),
]
