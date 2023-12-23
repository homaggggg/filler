from django.contrib import admin
from mysite.docgurnal.models import gurnal

# Register your models here.

class gurnalAdmin(admin.ModelAdmin):
	ttt = ('id', 'fiostud', 'facul', 'kafedra', 'groupnumber', 'napravlenie', 'vidpract', 'rukpractic', 'familinic', 'datasdacha', 'datanach', 'datakonec', 'predpriat', 'zadanie', 'dataotziv')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(gurnal, gurnalAdmin)

