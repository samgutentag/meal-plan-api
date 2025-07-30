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

## Environment Variables

- `ICAL_URL`: Your Google Calendar ICS feed URL (required)
