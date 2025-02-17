# Personal RSS Feed
This project allows you to aggregate RSS feeds and view them in a clean, user-friendly HTML page. Perfect for managing and customizing your personal news feed.

Features
- Aggregate articles from multiple RSS feeds into a single file.
- Clean HTML interface to display and read feeds.
- Simple to customize fonts, colors, and RSS sources.
- Optional archive directory (folder) for old RSS feeds.

## Getting Started

### 1. Installation
Ensure you have **Python 3.x** installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rss-feed
   cd rss-feed
   ```
2. Install dependencies (if any, though none are currently required):
   ```sh
   pip install -r requirements.txt  # If future dependencies are added
   ```

### 2. Generate a New RSS Feed:

- Open a terminal or command prompt in the project directory.
- Run the following command:

   ```sh
   python generate_rss_feed.py
   ```

- A new **aggregated_feed_YYYYMMDD_HHMMSS.xml** file will be created in the directory.

### 3. View Your Feed:

1. Open `rss_display.html` in a web browser.
2. Click the "Choose File" button and select the **aggregated XML file**.
3. The feed will be displayed with headlines, descriptions, and links to full articles.

### 4. Organize Feeds:

- Move older feeds into an **RSS Archive** folder to keep your workspace clean.

## Customization

### Modify RSS Sources
- Edit the `generate_rss_feed.py` script and update the `feed_urls` list with the RSS sources of your choice.

### Customize HTML Appearance
- Modify fonts, colors, and layout in the `<style>` section of `rss_display.html`.

### Change Background Image
- Replace `background.png` with any image of your choice to update the UI background.

## System Requirements
- **Python 3.x**
- A modern web browser (Chrome, Firefox, Edge, etc.)

## Troubleshooting

### Errors While Running `generate_rss_feed.py`
- Ensure you have an active internet connection to fetch RSS feeds.
- If an error occurs while parsing a feed, check if the RSS URL is valid.
- Update Python if you are running an older version.

### RSS Feed Not Displaying in Browser
- Ensure the generated XML file is correctly formatted.
- Try opening the file in a text editor to verify its structure.
- Make sure JavaScript is enabled in your browser.


