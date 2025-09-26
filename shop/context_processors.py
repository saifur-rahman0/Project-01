from .models import LatestNews


def latest_news(request):
    """Return active latest-news items and a single text string for marquee compatibility."""
    try:
        news_qs = LatestNews.objects.filter(is_active=True).order_by('-created_at')[:10]
        news_list = [{'id': n.id, 'title': n.title, 'created_at': n.created_at} for n in news_qs]
        first_text = news_list[0]['title'] if news_list else ''
        return {'LATEST_NEWS_LIST': news_list, 'LATEST_NEWS_TEXT': first_text}
    except Exception:
        # During migrations or before DB ready, avoid throwing errors in templates
        return {'LATEST_NEWS_LIST': [], 'LATEST_NEWS_TEXT': ''}
