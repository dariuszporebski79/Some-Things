from django.contrib import admin
from walks_and_talks.models import (Constituencies, AllocatingMandatesMethods,
                                    AllocatingMethodsAdvantages, AllocatingMethodsDisadvantages)


admin.site.register(Constituencies)
admin.site.register(AllocatingMandatesMethods)
admin.site.register(AllocatingMethodsAdvantages)
admin.site.register(AllocatingMethodsDisadvantages)
