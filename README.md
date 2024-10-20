# Flight Searcher

## Overview

Flight Searcher is a project developed to help me gain experience in building web applications that fetch and display flight information using Selenium. This project aims to provide a basic yet practical example of web scraping and backend development.

## Features

- **Search Flights**: Users can search for flights based on origin, destination, and travel dates using Google.
- **One-Way and Round-Trip Options**: Supports both one-way and round-trip flight searches.
- **Price Comparison**: Extracts and compares flight prices to find the cheapest option.

## Usage
- **Use the application via API**:
- **POST** request to /data with JSON body:
```Json
{
  "from": "origin",
  "goTo": "destination",
  "way": "one way or round trip",
  "date": "departure date",
  "returnDate": "return date (if round trip)"
}
```
- **GET** request to /data to check the server status.

## Technologies
-  **Web Scraping**: Selenium, BeautifulSoup
-  **Backend**: Flask
-  **Programming Language**: Python
