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
        return render(request, 'dHondt_method.html',
                      {"ctx": [electoral_committees, '']})

    def post(self, request):
        electoral_committees = ElectoralCommittee.objects.all()
        support = request.POST.getlist('support')
        sum_of_support = 0
        for s in support:
            sum_of_support += float(s)
        if ('' not in support) and (sum_of_support <= 100):
            committee_names = []
            are_coalitions = []
            # !!!other_committees!!!
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
                          {"ctx": [electoral_committees, results]})
        else:
            message = (f'''Coś poszło nie tak :-( ;-). Prawdopodobnie któreś pole zostało puste
                       albo suma poparcia dla komitetów wyborczych przekroczyła 100.
                       Spróbuj jeszcze raz :-)''')
            return render(request, 'dHondt_method.html',
                          {"ctx": [electoral_committees, "", message]})
    # (18.09) =>
    # def post(self, request):
    #     electoral_committees = ElectoralCommittee.objects.all()
    #     support = request.POST.getlist('support')
    #     if (('' not in support)
    #             and (float(support[0]) + float(support[1]) + float(support[2]) <= 100)):
    #         committee_names = []
    #         are_coalitions = []
    #         # !!!other_committees!!!
    #         for committee in electoral_committees:
    #             committee_names.append(committee.committee_name)
    #             are_coalitions.append(committee.is_coalition)
    #         committee_name_1 = committee_names[0]
    #         committee_name_2 = committee_names[1]
    #         committee_name_3 = committee_names[2]
    #         is_coalition_1 = are_coalitions[0]
    #         is_coalition_2 = are_coalitions[1]
    #         is_coalition_3 = are_coalitions[2]
    #         support_1 = float(support[0])
    #         support_2 = float(support[1])
    #         support_3 = float(support[2])
    #         if is_coalition_1 == False:
    #             if support_1 < 5:
    #                 result_1 = 'Brak mandatów. Komitet nie przekroczył progu 5%'
    #             else:
    #                 result_1 = round(support_1 * 460 / 100)
    #         else:
    #             if support_1 < 8:
    #                 result_1 = 'Brak mandatów. Komitet nie przekroczył progu 8%'
    #             else:
    #                 result_1 = round(support_1 * 460 / 100)
    #         if is_coalition_2 == False:
    #             if support_2 < 5:
    #                 result_2 = 'Brak mandatów. Komitet nie przekroczył progu 5%'
    #             else:
    #                 result_2 = round(support_2 * 460 / 100)
    #         else:
    #             if support_2 < 8:
    #                 result_2 = 'Brak mandatów. Komitet nie przekroczył progu 8%'
    #             else:
    #                 result_2 = round(support_2 * 460 / 100)
    #         if is_coalition_3 == False:
    #             if support_3 < 5:
    #                 result_3 = 'Brak mandatów. Komitet nie przekroczył progu 5%'
    #             else:
    #                 result_3 = round(support_3 * 460 / 100)
    #         else:
    #             if support_3 < 8:
    #                 result_3 = 'Brak mandatów. Komitet nie przekroczył progu 8%'
    #             else:
    #                 result_3 = round(support_3 * 460 / 100)
    #         electoral_committee_1 = [committee_name_1, support_1, result_1]
    #         electoral_committee_2 = [committee_name_2, support_2, result_2]
    #         electoral_committee_3 = [committee_name_3, support_3, result_3]
    #         results = [electoral_committee_1, electoral_committee_2, electoral_committee_3]
    #         return render(request, 'dHondt_method.html',
    #                       {"ctx": [electoral_committees, results]})
    #     else:
    #         message = (f'''Coś poszło nie tak :-( ;-). Prawdopodobnie któreś pole zostało puste
    #                    albo suma poparcia dla komitetów wyborczych przekroczyła 100.
    #                    Spróbuj jeszcze raz :-)''')
    #         return render(request, 'dHondt_method.html',
    #                       {"ctx": [electoral_committees, "", message]})
    # <= (18.09)


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
