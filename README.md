# Meal Plan API

A simple API that fetches meal planning data from a Google Calendar ICS feed and serves it as JSON.

## Features

- Fetches meal data from Google Calendar ICS feed
- Filters for current week (Monday to Sunday)
- Maps calendar events to meal types based on time:
  - Breakfast: 8 AM
  - KidLunch: 11 AM
  - Lunch: 12 PM
  - Dinner: 5 PM
- Outputs structured JSON with day indices (0-6) as keys
- Handles timezone conversion (UTC to PST/PDT)

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Google Calendar ICS URL:
   ```
   ICAL_URL=https://calendar.google.com/calendar/ical/YOUR_CALENDAR_ID/basic.ics
   ```
4. Run the script:
   ```bash
   python app.py
   ```

## Output Format

The script generates a `meals.json` file with the following structure:

```json
{
  "today": {
    "Breakfast": "",
    "KidLunch": "SunButter Energy Bites",
    "Lunch": "Crispy Cabbage Pancakes",
    "Dinner": "Chicken Tikka Masala",
    "TodayDate": "December 15, 2024"
  },
  "0": {
    "Breakfast": "",
    "KidLunch": "SunButter Energy Bites",
    "Lunch": "Crispy Cabbage Pancakes",
    "Dinner": "Chicken Tikka Masala"
  },
  "1": {
    "Breakfast": "",
    "KidLunch": "Mama French Toast",
    "Lunch": "Crispy Cabbage Pancakes",
    "Dinner": "Chicken Tikka Masala"
  }
  // ... continues for days 2-6
}
```

### Today Key

The `"today"` key contains meal information for the current day only, including:

- `Breakfast`: Breakfast meal for today
- `KidLunch`: Kid's lunch for today
- `Lunch`: Lunch meal for today
- `Dinner`: Dinner meal for today
- `TodayDate`: Formatted date string (e.g., "December 15, 2024")

### Day Mapping

- `0`: Monday
- `1`: Tuesday
- `2`: Wednesday
- `3`: Thursday
- `4`: Friday
- `5`: Saturday
- `6`: Sunday

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that runs the script daily and commits the updated `meals.json` file.

## Usage as API

This repository is configured to serve the `meals.json` file as a static API endpoint via GitHub Pages.

### Setup GitHub Pages

1. Go to your repository Settings → Pages
2. Under "Source", select "Deploy from a branch"
3. Choose the `main` branch
4. Click "Save"

Your API will be available at:
`https://yourusername.github.io/meal-plan-api/meals.json`

### Alternative Hosting

You can also serve the `meals.json` file using other static hosting services:

## TRMNL E-Ink Display Layouts

The `trmnl/` directory contains layout files designed for use with e-ink displays from [usetrmnl.com](https://usetrmnl.com). These Liquid template files provide different visual layouts for displaying meal plan data on e-ink screens.

### Available Layouts

- `trmnl_plugin.liquid`: Full week view with meal types as rows and days as columns
- Additional layout files may be available for different display configurations

### Usage with TRMNL

1. Configure your TRMNL device to point to your meal plan API endpoint
2. Select the appropriate layout file based on your display preferences
3. The layouts will automatically fetch and display the meal data from your API

### Layout Features

- Responsive grid layouts optimized for e-ink displays
- Automatic data binding to meal plan JSON structure
- Support for both full week view and today-only views
- Clean, readable typography for e-ink screens

## Environment Variables

- `ICAL_URL`: Your Google Calendar ICS feed URL (required)
