from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/', views.MenuItemsView.as_view(), name='menu_api'),
    path('bookings/', views.BookingView.as_view(), name='booking_api'), 
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('menus/', views.MenuView.as_view(), name='menus'),
    path('menus/<int:pk>/', views.SingleMenuView.as_view(), name='single_menu'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='single_booking'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
