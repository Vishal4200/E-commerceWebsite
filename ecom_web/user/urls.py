from . import views
from django.urls import path,re_path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf.urls import url,include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    
    path('edit_profile',views.edit_profile,name='edit_profile'),
    
    # password reset url's
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password-change', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('password-reset/confirm//<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
         email_template_name = 'registration/password_reset_email.html',
         success_url = reverse_lazy('user:password_reset_done')),name='password_reset'),
    
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    

    

]