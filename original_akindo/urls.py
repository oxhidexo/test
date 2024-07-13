from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  # Use absolute import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),  # Route for the home page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
]