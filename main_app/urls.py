from django.urls import path
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='cars_index'),
    path('aftermarket/', views.AftermarketIndex.as_view(), name='aftermarket_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
    path('aftermarket/<int:pk>/', views.AftermarketDetail.as_view(), name='aftermarket_detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('aftermarket/create/', views.AftermarketCreate.as_view(), name='aftermarket_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('aftermarket/<int:pk>/update/', views.AftermarketUpdate.as_view(), name='aftermarket_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('aftermarket/<int:pk>/delete/', views.AftermarketDelete.as_view(), name='aftermarket_delete'),
    path('cars/<int:car_id>/add_oilchange/', views.add_oilchange, name='add_oilchange'),
    path('cars/<int:car_id>/assoc_aftermarket/<int:aftermarket_id>/', views.assoc_aftermarket, name='assoc_aftermarket'),
    path('cars/<int:car_id>/del_aftermarket/<int:aftermarket_id>/', views.del_aftermarket, name='del_aftermarket'),
    path('accounts/signup/', views.signup, name='signup'),
]