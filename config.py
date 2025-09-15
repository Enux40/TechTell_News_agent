"""Configuration settings for TechTell News Agent."""

# Default news sources (RSS feeds)
DEFAULT_NEWS_SOURCES = {
    'techcrunch': 'https://techcrunch.com/feed/',
    'ars_technica': 'https://feeds.arstechnica.com/arstechnica/index',
    'hacker_news': 'https://hnrss.org/frontpage',
    'the_verge': 'https://www.theverge.com/rss/index.xml',
    'wired': 'https://www.wired.com/feed/rss'
}

# Application settings
DEFAULT_ARTICLE_LIMIT = 10
DEFAULT_OUTPUT_FORMAT = 'text'  # 'text' or 'json'
DEFAULT_CACHE_DURATION = 3600  # 1 hour in seconds

# Display settings
TITLE_MAX_LENGTH = 80
DESCRIPTION_MAX_LENGTH = 200