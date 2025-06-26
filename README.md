# News Headlines Web Scraper

A Python-based web scraper that extracts news headlines from Times of India's website. This project was created as part of Task 3 for the Elevate Labs Internship.

## Features

- Scrapes headlines from Times of India's website
- Saves headlines to a text file
- Uses BeautifulSoup4 for HTML parsing
- Simple and automated headline extraction
- Persistent storage of headlines

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install beautifulsoup4 requests
   ```

## How to Use

1. Make sure you have installed all requirements
2. Run the scraper:
   ```bash
   python main.py
   ```
3. The script will:
   - Connect to Times of India's website
   - Extract the latest headline
   - Save it to `headlines.txt`
   - Display a confirmation message

## Project Structure

- `main.py`: Main program file containing the web scraping logic
- `headlines.txt`: File that stores the scraped headlines
- `LICENSE`: Project license file
- `README.md`: This documentation file

## How it Works

The application uses:
- `requests` library to fetch the webpage content
- `BeautifulSoup4` to parse the HTML and extract headlines
- File I/O operations to save headlines persistently
- HTML parsing to locate and extract specific content

### Technical Details

- The scraper targets the Times of India website (timesofindia.indiatimes.com)
- Headlines are extracted from the `figcaption` tags
- Headlines are appended to `headlines.txt` with each run
- Simple error handling for web requests

## Important Notes

- Be mindful of the website's robots.txt and scraping policies
- The script is designed for educational purposes
- Website structure changes may require script updates
- Consider implementing rate limiting for production use

## Future Improvements

Possible enhancements could include:
- Multiple news source support
- Scheduled scraping
- Date and time stamping for headlines
- Category-based headline sorting
- JSON/CSV export options
- Error logging
- Rate limiting implementation
- Web interface for viewing headlines
