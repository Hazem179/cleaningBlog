from django.contrib import admin
from .models import Categories, SubCategories,Post,About,ServiceCities,FrequentlyQuestions

# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Post)
admin.site.register(ServiceCities)
admin.site.register(FrequentlyQuestions)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('phone_number','state')
    list_filter = ('state',)
    list_editable = ('state',)

admin.site.register(About,AboutAdmin)
