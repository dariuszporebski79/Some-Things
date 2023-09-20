from django.contrib import admin
from walks_and_talks.models import (Constituencies, AllocatingMandatesMethods,
                                    AllocatingMethodsAdvantages, AllocatingMethodsDisadvantages,
                                    ElectoralCommittee, People)


admin.site.register(Constituencies)
admin.site.register(AllocatingMandatesMethods)
admin.site.register(AllocatingMethodsAdvantages)
admin.site.register(AllocatingMethodsDisadvantages)
admin.site.register(ElectoralCommittee)
admin.site.register(People)
