from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as account_views

urlpatterns =[
    # path('login', views.user_login, name='login'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login', auth_views.logout_then_login, name='logout-then-login'),
    path('', account_views.dashboard, name='dashboard'),
    path('password-change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register', account_views.register, name='register'),
    path('edit', account_views.edit, name='edit')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
