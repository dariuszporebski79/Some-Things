"""
URL configuration for some_things project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from walks_and_talks.views import (WelcomeSiteView, WalksAndTalksCategoriesView,
                                   SocietyWalksAndTalksView, OpinionsAboutDemocracyView,
                                   DHondtMethodView, AddElectoralCommitteeView,
                                   EditElectoralCommitteeView, DeleteElectoralCommitteeView,
                                   MethodsAdvantagesAndDisadvantagesView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeSiteView.as_view(), name='welcome'),
    path('walksandtalks/', WalksAndTalksCategoriesView.as_view(), name='walks-and-talks'),
    path('society/', SocietyWalksAndTalksView.as_view(), name='society'),
    path('society/aboutdemocracy/', OpinionsAboutDemocracyView.as_view(), name='about-democracy'),
    path('society/dHondt/', DHondtMethodView.as_view(), name='dHondt'),
    path('society/addcommittee/', AddElectoralCommitteeView.as_view(), name='add-committee'),
    path('society/editcommittee/<int:committee_id>/', EditElectoralCommitteeView.as_view(),
         name='edit-committee'),
    path('society/deletecommittee/<int:committee_id>/', DeleteElectoralCommitteeView.as_view(),
         name='delete-committee'),
    path('society/aboutmethods/', MethodsAdvantagesAndDisadvantagesView.as_view(),
         name='about-methods'),
    path('accounts/', include('django.contrib.auth.urls')),
]
