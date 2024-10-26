from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from article.forms import ArticleForm
from article.models import Article
from pytils.translit import slugify


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('article:articles_list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        # Получаем текущий объект статьи
        article = self.object
        # Формируем URL для перенаправления на страницу деталей статьи
        return reverse_lazy('article:articles_detail', kwargs={'pk': article.pk})

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.number_of_views > 1:
            self.object.number_of_views -= 1
            self.object.save()
        return self.object




class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:articles_list')