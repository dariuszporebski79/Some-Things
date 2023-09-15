from django.shortcuts import render, redirect
from django.views import View
from walks_and_talks.models import ElectoralCommittee


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
        # message = "Hello!"
        electoral_committees = ElectoralCommittee.objects.all()
        return render(request, 'dHondt_method.html', {"ctx": electoral_committees})

    def post(self, request):
        pass


class AddElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'add_electoral_committee.html')

    def post(self, request):
        committee_name = request.POST.get("committee_name")
        is_coalition = request.POST.get("is_coalition")
        if ((committee_name and not ElectoralCommittee.objects.filter(committee_name=committee_name))
                and is_coalition):
            if is_coalition == "Yes":
                is_coalition = True
            else:
                is_coalition = False
            new_committee = ElectoralCommittee.objects.create(committee_name=committee_name,
                                                              is_coalition=is_coalition)
            # message = f"""Great, you have just added a new ...
            # Name: ..."""
            return redirect('dHondt')
            # return render(request, ".html", context={"message": message})
        else:
            message = f"Coś poszło nie tak :-( ;-). Spróbuj jeszcze raz :-)"
            return render(request, 'add_electoral_committee.html',
                          {"message": message})


class EditElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'edit_elecoral_committee.html')


class DeleteElectoralCommitteeView(View):
    def get(self, request):
        return render(request, 'delete_electoral_committee.html')
