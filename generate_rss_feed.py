import feedparser  # Library to parse RSS feeds
from datetime import datetime  # Library to handle date and time

# List of RSS feed URLs
# Replace these URLs with the RSS feeds you want to include in the aggregation
feed_urls = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",  # BBC World News
    "https://rss.cnn.com/rss/edition.rss",  # CNN International
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",  # NY Times Homepage
    "https://www.reutersagency.com/en/reutersbest/reuters-best-rss-feeds/",  # Reuters Best
    "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera All News
    "https://rss.csmonitor.com/feeds/all",  # Christian Science Monitor
    "https://www.thebureauinvestigates.com/stories?format=rss",  # The Bureau of Investigative Journalism
    "https://www.pewresearch.org/feed/",  # Pew Research
    "https://theintercept.com/feed/?rss",  # The Intercept
    "https://www.propublica.org/feeds/"  # ProPublica
]

# RSS feed template - Defines the structure of the final RSS file
rss_template = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>Private News Feed</title>  <!-- Feed title -->
    <description>Aggregated news updates</description>  <!-- Description of your feed -->
    <lastBuildDate>{last_build_date}</lastBuildDate>  <!-- Timestamp of the feed generation -->
    {items}
  </channel>
</rss>
"""

# Template for individual RSS items - Defines the format of each news article
item_template = """
<item>
  <title>{title}</title>  <!-- News article title -->
  <link>{link}</link>  <!-- URL to the full article -->
  <description>{description}</description>  <!-- Article summary -->
  <author>{author}</author>  <!-- Article author -->
  <pubDate>{pub_date}</pubDate>  <!-- Date published -->
  <guid>{link}</guid>  <!-- Unique identifier for the article -->
</item>
"""

# Function to extract author information from each RSS entry
def extract_author(entry):
    """Extracts the author from an RSS entry, if available."""
    if hasattr(entry, "author"):
        return entry.author
    elif "dc:creator" in entry:
        return entry["dc:creator"]
    return "Unknown author"  # Default if no author is found

# Initialize list to store parsed RSS items
aggregated_items = []

# Iterate through each RSS feed URL
for url in feed_urls:
    try:
        feed = feedparser.parse(url)  # Parse the RSS feed
        for entry in feed.entries[:5]:  # Limit to 5 most recent articles per feed
            pub_date = getattr(entry, "published", "No Date")  # Extract publish date
            author = extract_author(entry)  # Extract author
            description = getattr(entry, "summary", "No description available")  # Extract summary

            # Append formatted RSS item to list
            aggregated_items.append(
                item_template.format(
                    title=entry.title,
                    link=entry.link,
                    description=description,
                    author=author,
                    pub_date=pub_date,
                )
            )
    except Exception as e:
        print(f"Error parsing feed from {url}: {e}")  # Debugging message

# Generate final RSS feed with aggregated items
rss_feed = rss_template.format(
    last_build_date=datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S +0000"),
    items="".join(aggregated_items)  # Concatenate all parsed items
)

# Generate timestamp for unique file naming
timestamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S")
file_name = f"aggregated_feed_{timestamp}.xml"  # Name output file

# Save the generated RSS feed to a file
with open(file_name, "w", encoding="utf-8") as file:
    file.write(rss_feed)

# Print success message with file name
print(f"RSS feed generated and saved as {file_name}")
