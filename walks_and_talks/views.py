from django.shortcuts import render
from django.views import View


class WelcomeSiteView(View):
    def get(self, request):
        return render(request, 'welcome_site.html')


class WalksAndTalksCategoriesView(View):
    def get(self, request):
        return render(request, 'walks_and_talks_categories.html')


class SocietyWalksAndTalksView(View):
    def get(self, request):
        return render(request, 'society_walks_and_talks.html')


class OpinionsAboutDemocracyView(View):
    def get(self, request):
        return render(request, 'opinions_about_democracy.html')


class DHondtMethodView(View):
    def get(self, request):
        return render(request, 'dHondt_method.html')


class AddElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'add_electoral_committee.html')


class EditElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'edit_elecoral_committee.html')


class DeleteElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'delete_electoral_committee.html')
