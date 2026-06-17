from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacancy, Article
from .forms import ArticleForm
import requests

def home(request):
    latest_vacancies = Vacancy.objects.filter(is_active=True).order_by('-created_at')[:3]
    latest_articles = Article.objects.order_by('-created_at')[:3]
    return render(request, 'jobs/index.html', {
        'vacancies': latest_vacancies,
        'articles': latest_articles
    })

def vacancies_list(request):
    query = request.GET.get('q')
    if query:
        all_vacancies = Vacancy.objects.filter(title__icontains=query, is_active=True)
    else:
        all_vacancies = Vacancy.objects.filter(is_active=True)
        
    return render(request, 'jobs/vacancies.html', {'vacancies': all_vacancies, 'query': query})

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, 'jobs/detail.html', {'vacancy': vacancy})

def articles_list(request):
    all_articles = Article.objects.order_by('-created_at')
    return render(request, 'jobs/articles.html', {'articles': all_articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'jobs/article_detail.html', {'article': article})

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    return render(request, 'jobs/add_article.html', {'form': form})

def about(request):
    return render(request, 'jobs/about.html')

def jooble_vacancies(request):
    keywords = request.GET.get("q", "Python")

    url = "https://jooble.org/api/5eeee30b-bd44-4919-b8a8-f94166165284"

    response = requests.post(
        url,
        json={
            "keywords": keywords,
            "location": "",
        }
    )

    vacancies = []

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("jobs", [])

    return render(
        request,
        "jobs/jooble_vacancies.html",
        {
            "vacancies": vacancies,
            "query": keywords
        }
    )