from django.urls import path, include
from .views import (
    UserView, 
    RegisterView,
)

  
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')), 
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', RegisterView, basename="register") # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser

urlpatterns += router.urls
