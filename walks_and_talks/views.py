from django.shortcuts import render
from django.views import View


class WelcomeSiteView(View):
    def get(self, request):
        return render(request, "welcome_site.html")


class WalksAndTalksCategoriesView(View):
    def get(self, request):
        return render(request, "welcome_site.html")


class SocietyWalksAndTalksView(View):
    def get(self, request):
        return render(request, "society_walks_and_talks.html")


class OpinionsAboutDemocracyView(View):
    def get(self, request):
        return render(request, "society_walks_and_talks.html")


class DHondtMethodView(View):
    def get(self, request):
        return render(request, "dHondt_method.html")
