from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.urls import path
from case_management import views

# Admin Site Config
admin.site.site_header = "NZ Health Admin"
admin.site.site_title = "NZ Health Admin Portal"
admin.site.index_title = "Welcome to NZ Health Researcher Portal"


urlpatterns = [    
    path('admin/', admin.site.urls, name ='admin'), 
    path('accounts/', include('django.contrib.auth.urls')),   
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('create_person',views.create_person, name='create_person'),
    path('people',views.people, name="show_people"),
    path('edit_person/<int:id>',views.edit_person),    
    path('delete_person/<int:id>',views.delete_person),
    path('update_person/<int:id>',views.update_person),   
    path('show_person/<int:id>',views.show_person, name='show_person'), 
    path('create_referral/',views.create_referral, name='create_referral'),
    path('referrals',views.referrals, name='referrals'),
    path('edit_referral/<int:id>',views.edit_referral),   
    path('update_referral/<int:id>',views.update_referral),
    path('delete_referral/<int:id>',views.delete_referral),
    path('show_referral/<int:id>',views.show_referral, name="show_referral"), 
]

