from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Category, Article, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if not dictionary.get('main'):
                continue
            elif dictionary['main'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Вы не указали главную категорию')
        elif i > 1:
            raise ValidationError('Главной категорией может быть только одна')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
