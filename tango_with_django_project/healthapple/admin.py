from django.contrib import admin
from healthapple.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'summary', 'url', 'flesch_score', 'sentiment_score', 'subjectivity_score',)

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)