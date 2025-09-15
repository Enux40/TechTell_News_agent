"""Test data for TechTell News Agent when RSS feeds are not accessible."""

from datetime import datetime, timezone

# Mock news data for testing
MOCK_NEWS_DATA = {
    'techcrunch': [
        {
            'title': 'AI Startup Raises $100M Series A',
            'link': 'https://techcrunch.com/ai-startup-funding',
            'description': 'A revolutionary AI startup focused on natural language processing has raised $100 million in Series A funding.',
            'published': datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc),
            'source': 'techcrunch'
        },
        {
            'title': 'New iPhone Features Leaked',
            'link': 'https://techcrunch.com/iphone-leak',
            'description': 'Latest leaks reveal exciting new features coming to the next iPhone release.',
            'published': datetime(2024, 1, 15, 9, 15, tzinfo=timezone.utc),
            'source': 'techcrunch'
        }
    ],
    'hacker_news': [
        {
            'title': 'Show HN: I built a news aggregator',
            'link': 'https://news.ycombinator.com/item?id=123456',
            'description': 'After being frustrated with existing news apps, I decided to build my own.',
            'published': datetime(2024, 1, 15, 11, 0, tzinfo=timezone.utc),
            'source': 'hacker_news'
        },
        {
            'title': 'The Future of Programming Languages',
            'link': 'https://news.ycombinator.com/item?id=123457',
            'description': 'A deep dive into emerging programming languages and their potential impact.',
            'published': datetime(2024, 1, 15, 8, 45, tzinfo=timezone.utc),
            'source': 'hacker_news'
        }
    ],
    'the_verge': [
        {
            'title': 'Electric Vehicle Sales Surge',
            'link': 'https://theverge.com/ev-sales',
            'description': 'Electric vehicle sales have reached an all-time high this quarter.',
            'published': datetime(2024, 1, 15, 10, 0, tzinfo=timezone.utc),
            'source': 'the_verge'
        }
    ]
}