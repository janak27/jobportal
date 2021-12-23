from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Candidate, CandidateJobMap
from import_export import resources




class CandidateResource(resources.ModelResource):
    class Meta:
        model = Candidate
    


class CandidateAdmin(ImportExportModelAdmin):
    resource_class = CandidateResource
    list_display = ('name','mobile','age','gender','will_relocate','city','is_engaged')
    list_filter = ('city', 'gender', 'will_relocate','age')
    resource_class = CandidateResource

class ReviewCandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'age', 'gender', 'city', 'status')
    list_filter = ('job','status')
    list_editable = ('status',)
    list_display_links = None


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateJobMap, ReviewCandidateAdmin)
 
 