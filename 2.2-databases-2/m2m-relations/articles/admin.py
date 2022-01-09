from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        kol = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            print(form.cleaned_data)
            # print('is_main:', form.cleaned_data['is_main'])
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

            if form.cleaned_data:
                print('form.cleaned_data[tag]', form.cleaned_data['tag'])
                if form.cleaned_data['is_main']:
                    kol += 1

        if kol != 1:
            raise ValidationError('Не выполнена валидация формы. Возможен только один и только один основной тэг.')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
