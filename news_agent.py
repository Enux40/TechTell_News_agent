"""TechTell News Agent - A simple technology news aggregator."""

import feedparser
import requests
import json
from datetime import datetime, timezone
from dateutil import parser as date_parser
from colorama import init, Fore, Style
from typing import List, Dict, Optional
import time

from config import DEFAULT_NEWS_SOURCES, DEFAULT_ARTICLE_LIMIT, DEFAULT_CACHE_DURATION
try:
    from test_data import MOCK_NEWS_DATA
except ImportError:
    MOCK_NEWS_DATA = {}


class NewsAgent:
    """Main news agent class for fetching and displaying tech news."""
    
    def __init__(self, sources: Optional[Dict[str, str]] = None, test_mode: bool = False):
        """Initialize the news agent with news sources."""
        self.sources = sources or DEFAULT_NEWS_SOURCES
        self.cache = {}
        self.cache_timestamps = {}
        self.test_mode = test_mode
        init()  # Initialize colorama for colored output
    
    def fetch_news(self, source_name: str) -> List[Dict]:
        """Fetch news from a specific source."""
        if source_name not in self.sources:
            raise ValueError(f"Unknown news source: {source_name}")
        
        # Check cache first
        if self._is_cache_valid(source_name):
            return self.cache[source_name]
        
        # Use mock data in test mode
        if self.test_mode and source_name in MOCK_NEWS_DATA:
            articles = MOCK_NEWS_DATA[source_name]
            self.cache[source_name] = articles
            self.cache_timestamps[source_name] = time.time()
            return articles
        
        url = self.sources[source_name]
        try:
            print(f"Fetching news from {source_name}...")
            feed = feedparser.parse(url)
            
            articles = []
            for entry in feed.entries:
                article = {
                    'title': entry.get('title', 'No title'),
                    'link': entry.get('link', ''),
                    'description': self._clean_description(entry.get('summary', '')),
                    'published': self._parse_date(entry.get('published', '')),
                    'source': source_name
                }
                articles.append(article)
            
            # Cache the results
            self.cache[source_name] = articles
            self.cache_timestamps[source_name] = time.time()
            
            return articles
            
        except Exception as e:
            print(f"Error fetching news from {source_name}: {e}")
            # Fallback to mock data if available
            if source_name in MOCK_NEWS_DATA:
                print(f"Using mock data for {source_name}")
                return MOCK_NEWS_DATA[source_name]
            return []
    
    def fetch_all_news(self, limit: int = DEFAULT_ARTICLE_LIMIT) -> List[Dict]:
        """Fetch news from all configured sources."""
        all_articles = []
        
        for source_name in self.sources:
            articles = self.fetch_news(source_name)
            all_articles.extend(articles)
        
        # Sort by published date (newest first)
        all_articles.sort(key=lambda x: x['published'], reverse=True)
        
        return all_articles[:limit]
    
    def display_news(self, articles: List[Dict], format_type: str = 'text'):
        """Display news articles in the specified format."""
        if format_type == 'json':
            self._display_json(articles)
        else:
            self._display_text(articles)
    
    def _display_text(self, articles: List[Dict]):
        """Display articles in colored text format."""
        if not articles:
            print(f"{Fore.YELLOW}No articles found.{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.CYAN}{'='*80}")
        print(f"TechTell News Agent - {len(articles)} Latest Articles")
        print(f"{'='*80}{Style.RESET_ALL}\n")
        
        for i, article in enumerate(articles, 1):
            print(f"{Fore.GREEN}[{i}] {article['title'][:80]}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}Source: {article['source']} | Published: {article['published']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}{article['description'][:200]}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}Link: {article['link']}{Style.RESET_ALL}")
            print(f"{'-'*80}\n")
    
    def _display_json(self, articles: List[Dict]):
        """Display articles in JSON format."""
        output = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'article_count': len(articles),
            'articles': articles
        }
        print(json.dumps(output, indent=2, default=str))
    
    def _clean_description(self, description: str) -> str:
        """Clean HTML tags and limit description length."""
        import re
        # Remove HTML tags
        clean_desc = re.sub('<.*?>', '', description)
        # Remove extra whitespace
        clean_desc = ' '.join(clean_desc.split())
        return clean_desc
    
    def _parse_date(self, date_string: str) -> datetime:
        """Parse date string into datetime object."""
        if not date_string:
            return datetime.now(timezone.utc)
        
        try:
            return date_parser.parse(date_string)
        except Exception:
            return datetime.now(timezone.utc)
    
    def _is_cache_valid(self, source_name: str) -> bool:
        """Check if cached data is still valid."""
        if source_name not in self.cache or source_name not in self.cache_timestamps:
            return False
        
        cache_age = time.time() - self.cache_timestamps[source_name]
        return cache_age < DEFAULT_CACHE_DURATION
    
    def list_sources(self):
        """List all available news sources."""
        print(f"\n{Fore.CYAN}Available News Sources:{Style.RESET_ALL}")
        for source_name, url in self.sources.items():
            print(f"{Fore.GREEN}• {source_name}: {url}{Style.RESET_ALL}")
        print()


if __name__ == "__main__":
    # Simple test/demo
    agent = NewsAgent()
    print("TechTell News Agent - Demo Mode")
    agent.list_sources()
    
    # Fetch and display latest news
    articles = agent.fetch_all_news(limit=5)
    agent.display_news(articles)