from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rango import views


app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>', views.add_page, name='add_page'),
    # path('search/', views.search, name='search'),
    # path('register/', views.register, name='register'),
    path('goto/', views.track_url, name='goto'),
    path('profile_registration/', views.register_profile, name='profile_registration'),
    path('about/', views.about, name='about'),
    path('profile/<username>', views.profile, name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category'),
    path('add/', views.auto_add_page, name='auto_add_page'),
] 