# TechTell News Agent 🚀📰

A lightweight Python-based technology news aggregator that fetches and displays the latest tech news from multiple sources.

## Features

- 📡 Fetches news from multiple technology news sources
- 🎨 Colorized terminal output for better readability
- 💾 Smart caching to avoid excessive API calls
- 🔧 Command-line interface with multiple options
- 📄 JSON and text output formats
- ⚡ Fast and lightweight

## Supported News Sources

- **TechCrunch** - Latest startup and technology news
- **Ars Technica** - In-depth technology analysis
- **Hacker News** - Community-driven tech discussions
- **The Verge** - Technology and culture news
- **Wired** - Technology trends and innovation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Enux40/TechTell_News_agent.git
   cd TechTell_News_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

#### Fetch Latest News
```bash
# Get 10 latest articles (default)
python cli.py fetch

# Get 5 latest articles
python cli.py fetch --limit 5

# Get news in JSON format
python cli.py fetch --format json

# Get news from specific source
python cli.py fetch --source techcrunch
```

#### List Available Sources
```bash
python cli.py sources
```

#### Add Custom Source (temporary)
```bash
python cli.py add-source "my_source" "https://example.com/rss"
```

#### Run Demo
```bash
python cli.py demo
```

### Python Module Usage

```python
from news_agent import NewsAgent

# Create news agent instance
agent = NewsAgent()

# Fetch news from all sources
articles = agent.fetch_all_news(limit=10)

# Display in terminal
agent.display_news(articles)

# Display in JSON format
agent.display_news(articles, format_type='json')

# Fetch from specific source
techcrunch_news = agent.fetch_news('techcrunch')
```

## Configuration

The application uses `config.py` for default settings:

- **DEFAULT_ARTICLE_LIMIT**: Number of articles to fetch (default: 10)
- **DEFAULT_CACHE_DURATION**: Cache validity in seconds (default: 3600)
- **DEFAULT_NEWS_SOURCES**: Dictionary of news sources and their RSS URLs

## Project Structure

```
TechTell_News_agent/
├── news_agent.py      # Main NewsAgent class
├── cli.py             # Command-line interface
├── config.py          # Configuration settings
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- `requests` - HTTP library for API calls
- `feedparser` - RSS/Atom feed parser
- `python-dateutil` - Date parsing utilities
- `colorama` - Cross-platform colored terminal text
- `click` - Command-line interface creation toolkit

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- [ ] Web interface using Flask/FastAPI
- [ ] Database storage for articles
- [ ] Email notifications for breaking news
- [ ] Keyword filtering and search
- [ ] Social media integration
- [ ] Mobile app version

---

**Happy news reading! 📖✨**