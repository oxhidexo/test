from django.contrib import admin
from django.urls import path, include
from original_akindo.views import home  # Use absolute import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Route for the home page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
]
