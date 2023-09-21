from django.shortcuts import render, redirect
from django.views import View
from walks_and_talks.models import (ElectoralCommittee, AllocatingMethodsAdvantages,
                                    AllocatingMethodsDisadvantages, AllocatingMandatesMethods)


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
        method = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
        dHondt_advantages = method.allocatingmethodsadvantages_set.all()
        dHondt_disadvantages = method.allocatingmethodsdisadvantages_set.all()
        dHondt_creators = method.people_set.all()
        return render(request, 'dHondt_method.html',
                      {"ctx": [electoral_committees, dHondt_advantages,
                               dHondt_disadvantages, method, dHondt_creators, '']})

    def post(self, request):
        electoral_committees = ElectoralCommittee.objects.all()
        # dHondt_people = ''
        method = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
        dHondt_advantages = method.allocatingmethodsadvantages_set.all()
        dHondt_disadvantages = method.allocatingmethodsdisadvantages_set.all()
        dHondt_creators = method.people_set.all()
        support = request.POST.getlist('support')
        sum_of_support = 0
        if '' not in support:
            for s in support:
                sum_of_support += float(s)
        if ('' not in support) and (sum_of_support <= 100):
            committee_names = []
            are_coalitions = []
            for committee in electoral_committees:
                committee_names.append(committee.committee_name)
                are_coalitions.append(committee.is_coalition)
            index = 0
            results = []
            for committee in electoral_committees:
                committee_name = committee_names[index]
                is_coalition = are_coalitions[index]
                committee_support = float(support[index])
                if is_coalition == False:
                    if committee_support < 5:
                        result = 'Brak mandatów. Komitet nie przekroczył progu 5%'
                    else:
                        result = round(committee_support * 460 / 100)
                else:
                    if committee_support < 8:
                        result = 'Brak mandatów. Komitet nie przekroczył progu 8%'
                    else:
                        result = round(committee_support * 460 / 100)
                electoral_committee = [committee_name, committee_support, result]
                index += 1
                results.append(electoral_committee)
            return render(request, 'dHondt_method.html',
                          {"ctx": [electoral_committees, dHondt_advantages,
                                   dHondt_disadvantages, method, dHondt_creators, results]})
        else:
            message = (f'''Coś poszło nie tak :-( ;-). Prawdopodobnie któreś pole zostało puste
                       albo suma poparcia dla komitetów wyborczych przekroczyła 100.
                       Spróbuj jeszcze raz :-)''')
            return render(request, 'dHondt_method.html',
                          {"ctx": [electoral_committees, dHondt_advantages,
                                   dHondt_disadvantages, method, dHondt_creators, "", message]})


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


class MethodsAdvantagesAndDisadvantagesView(View):
    def get(self, request):
        return render(request, 'methods_advantages_and_disadvantages.html')

    def post(self, request):
        feature_of_method = request.POST.get('feature_of_method')
        advantage_or_disadvantage = request.POST.get('advantage_or_disadvantage')
        methods = request.POST.getlist('methods')
        if feature_of_method and advantage_or_disadvantage and methods:
            if advantage_or_disadvantage == 'advantage':
                new_advantage = AllocatingMethodsAdvantages.objects.create(
                    advantage=feature_of_method)
                if len(methods) == 1:
                    if methods[0] == 'dHondt':
                        method = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
                        new_advantage.methods.add(method)
                    else:
                        method = AllocatingMandatesMethods.objects.get(name="metoda Sainte-Laguë")
                        new_advantage.methods.add(method)
                else:
                    method_1 = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
                    method_2 = AllocatingMandatesMethods.objects.get(name="metoda Sainte-Laguë")
                    new_advantage.methods.set([method_1, method_2])
            else:
                new_disadvantage = AllocatingMethodsDisadvantages.objects.create(
                    disadvantage=feature_of_method)
                if len(methods) == 1:
                    if methods[0] == 'dHondt':
                        method = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
                        new_disadvantage.methods.add(method)
                    else:
                        method = AllocatingMandatesMethods.objects.get(name="metoda Sainte-Laguë")
                        new_disadvantage.methods.add(method)
                else:
                    method_1 = AllocatingMandatesMethods.objects.get(name="metoda d'Hondta")
                    method_2 = AllocatingMandatesMethods.objects.get(name="metoda Sainte-Laguë")
                    new_disadvantage.methods.set([method_1, method_2])
            return redirect('dHondt')
        else:
            message = f'''Coś poszło nie tak :-( ;-). Być może nie zostały 
            wypełnione/wybrane wszystkie pola. Spróbuj jeszcze raz :-)'''
            return render(request, 'methods_advantages_and_disadvantages.html',
                          {"message": message})
