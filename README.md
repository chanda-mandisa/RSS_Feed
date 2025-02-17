# Personal RSS Feed

This project allows you to aggregate RSS feeds and view them in a clean, user-friendly HTML page. Perfect for managing and customizing your personal news feed.

## Features
- Aggregate articles from multiple RSS feeds into a single file.
- Clean HTML interface to display and read feeds.
- Simple to customize fonts, colors, and RSS sources.
- Optional archive directory (folder) for old RSS feeds.

## Getting Started
This project enables users to generate and view custom RSS feeds by aggregating articles from multiple sources.

## Installation
### Clone the Repository
```sh
git clone https://github.com/chanda-mandisa/RSS_Feed.git
cd rss-feed
```

### Running the Script
1. Generate a new RSS feed:
   ```sh
   python generate_rss_feed.py
   ```
2. A new file, **aggregated_feed_YYYYMMDD_HHMMSS.xml**, will be created in the directory.

## System Requirements
- **Python 3.x**
- A modern web browser (Chrome, Firefox, Edge, etc.)

## Usage
### Viewing the RSS Feed
1. Open `rss_display.html` in a web browser.
2. Click the "Choose File" button and select the **aggregated XML file**.
3. The feed will be displayed with headlines, descriptions, and links to full articles.

### Organizing Feeds
- Move older feeds into an **RSS Archive** folder to keep your workspace clean.

## Customization
### Modify RSS Sources
- Edit `generate_rss_feed.py` and update the `feed_urls` list with your preferred RSS sources.

### Customize HTML Appearance
- Modify fonts, colors, and layout in the `<style>` section of `rss_display.html`.

### Change Background Image
- Replace `background.png` with any image of your choice to update the UI background.

## Troubleshooting
### Errors While Running `generate_rss_feed.py`
- Ensure you have an active internet connection to fetch RSS feeds.
- If an error occurs while parsing a feed, check if the RSS URL is valid.
- Update Python if you are running an older version.

### RSS Feed Not Displaying in Browser
- Ensure the generated XML file is correctly formatted.
- Try opening the file in a text editor to verify its structure.
- Make sure JavaScript is enabled in your browser.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues.

## Author
Developed by [chanda-mandisa].

