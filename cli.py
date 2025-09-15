#!/usr/bin/env python3
"""Command-line interface for TechTell News Agent."""

import click
from news_agent import NewsAgent
from config import DEFAULT_ARTICLE_LIMIT


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """TechTell News Agent - Your technology news aggregator."""
    pass


@cli.command()
@click.option('--limit', '-l', default=DEFAULT_ARTICLE_LIMIT, 
              help=f'Number of articles to fetch (default: {DEFAULT_ARTICLE_LIMIT})')
@click.option('--format', '-f', 'output_format', default='text', 
              type=click.Choice(['text', 'json']), 
              help='Output format (default: text)')
@click.option('--source', '-s', default=None, 
              help='Fetch from specific source only')
@click.option('--test', is_flag=True, 
              help='Use test mode with mock data')
def fetch(limit, output_format, source, test):
    """Fetch and display latest technology news."""
    agent = NewsAgent(test_mode=test)
    
    try:
        if source:
            if source not in agent.sources:
                click.echo(f"Error: Unknown source '{source}'")
                click.echo("Use 'techtell sources' to see available sources.")
                return
            articles = agent.fetch_news(source)[:limit]
        else:
            articles = agent.fetch_all_news(limit)
        
        agent.display_news(articles, output_format)
        
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
def sources():
    """List all available news sources."""
    agent = NewsAgent()
    agent.list_sources()


@cli.command()
@click.argument('source_name')
@click.argument('url')
def add_source(source_name, url):
    """Add a new news source (temporary for current session)."""
    agent = NewsAgent()
    agent.sources[source_name] = url
    click.echo(f"Added source '{source_name}': {url}")
    click.echo("Note: This change is temporary and will not persist between sessions.")


@cli.command()
def demo():
    """Run a quick demo of the news agent."""
    click.echo("Running TechTell News Agent demo...")
    agent = NewsAgent(test_mode=True)
    agent.list_sources()
    
    click.echo("Fetching 3 latest articles...")
    articles = agent.fetch_all_news(limit=3)
    agent.display_news(articles)


if __name__ == '__main__':
    cli()