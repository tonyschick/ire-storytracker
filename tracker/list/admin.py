from django.contrib import admin
from tracker.list.models import Article, Impact, Training, TrainingType


class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("headline",)}
	search_fields = ("headline", "organization", "byline", "description")
admin.site.register(Article, ArticleAdmin)

class ImpactAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
admin.site.register(Impact, ImpactAdmin)

class TrainingAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("city", "eventnumber",)}
	search_fields = ("city", "host")
	ordering = ('-date',)
admin.site.register(Training, TrainingAdmin)


class TrainingTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
admin.site.register(TrainingType, TrainingTypeAdmin)
