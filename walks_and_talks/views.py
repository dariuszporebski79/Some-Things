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
        electoral_committees = ElectoralCommittee.objects.all()
        support = "Coś tu się powinno kiedyś pojawić"
        return render(request, 'dHondt_method.html',
                      {"ctx": [electoral_committees, support]})

    def post(self, request):
        electoral_committees = ElectoralCommittee.objects.all()
        support = request.POST.getlist('support')
        return render(request, 'dHondt_method.html',
                      {"ctx": [electoral_committees, support]})

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
            return redirect('dHondt')
        else:
            message = f"Coś poszło nie tak :-( ;-). Spróbuj jeszcze raz :-)"
            return render(request, 'add_electoral_committee.html',
                          {"message": message})


class EditElectoralCommitteeView(View):
    def get(self, request, committee_id):
        edited_committee = ElectoralCommittee.objects.get(id=committee_id)
        message = ":-)"
        return render(request, 'edit_electoral_committee.html',
                      {"ctx": [message, edited_committee]})

    def post(self, request, committee_id):
        edited_committee = ElectoralCommittee.objects.get(id=committee_id)
        committee_name = request.POST.get("committee_name")
        is_coalition = request.POST.get("is_coalition")
        if ((committee_name and not ElectoralCommittee.objects.filter(committee_name=committee_name))
                or is_coalition):
            if (committee_name
                    and not ElectoralCommittee.objects.filter(committee_name=committee_name)):
                edited_committee.committee_name = committee_name
                edited_committee.save()
            if is_coalition:
                if is_coalition == "Yes":
                    is_coalition = True
                else:
                    is_coalition = False
                edited_committee.is_coalition = is_coalition
                edited_committee.save()
            return redirect('dHondt')
        else:
            message = f"Coś poszło nie tak :-( ;-). Spróbuj jeszcze raz :-)"
            return render(request, 'edit_electoral_committee.html',
                          {"ctx": [message, edited_committee]})


class DeleteElectoralCommitteeView(View):
    def get(self, request, committee_id):
        deleted_committee = ElectoralCommittee.objects.get(id=committee_id)
        deleted_committee.delete()
        return redirect('dHondt')
