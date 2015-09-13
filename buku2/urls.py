from django.conf.urls import patterns, url
from buku2 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^category/(?P<category_name>[\w\-]+)/$', views.category, name='category'),
	url(r'^category/(?P<category_name>[\w\-]+)/(?P<book_title>[\w\-]+)/$', views.book, name='book'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^add_book/category/(?P<category_name>[\w\-]+)/$', views.add_book, name='add_book'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
)  # New!)
