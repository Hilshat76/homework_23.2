from django.forms import ModelForm, BooleanField
from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-class'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

    words_to_check = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.words_to_check:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка. В названии используется недопустимые слова.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.words_to_check:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка В описании используется недопустимые слова.')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('is_active', 'description', 'category')


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')  # Получаем продукты из данных
        is_active = cleaned_data.get('is_active')  # Получаем статус активного

        if product and is_active:  # Проверьте, установлен ли продукт и активна ли эта версия
            # Проверьте наличие других активных версий
            active_versions = Version.objects.filter(product=product, is_active=True).exclude(pk=self.instance.pk)
            if active_versions.exists():
                raise forms.ValidationError(
                    'Ошибка: Для этого продукта уже существует активная версия. Пожалуйста, выберите только одну активную версию.')

        return cleaned_data
