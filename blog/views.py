from django.shortcuts import render
from articles.models import Article

def blog(request):
    recent_posts = Article.objects.live().all().select_related()[:5]
    return render(request, 'blog.html', dict(posts=recent_posts))

