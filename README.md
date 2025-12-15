# Meal Plan API

> [!TIP]
> Checkout my live gist at [https://gist.github.com/samgutentag/62b60125077a9cb53ea81ba517262185](https://gist.github.com/samgutentag/62b60125077a9cb53ea81ba517262185)

A simple API that fetches meal planning data from a Google Calendar ICS feed and serves it as JSON.

Meal data is now published to a private GitHub Gist, instead of a local file in the repository.

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
3. Create a `.env` file with your Google Calendar ICS URL and Gist credentials:

```
ICAL_URL=https://calendar.google.com/calendar/ical/YOUR_CALENDAR_ID/basic.ics
GIST_TOKEN=your_github_token_with_gist_scope
GIST_ID=your_gist_id   # (optional, if you want to update an existing Gist)
```

4. Run the script:

```bash
python app.py
```

## Output Format

The script writes the meal data to a GitHub Gist as `meals.json` with the following structure:

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

The repository can include a GitHub Actions workflow that runs the script daily and updates the Gist with the latest meal data. The workflow should provide the required environment variables (`ICAL_URL`, `GIST_TOKEN`, and optionally `GIST_ID`).

## Usage as API

You can access the meal data directly from the Gist URL. If the Gist is public, you can use the raw URL as an API endpoint. If the Gist is private, you will need to authenticate with your GitHub token to access the data programmatically.

### Example: Fetching the Gist

> [!IMPORTANT]
> Make sure your gist is set to **public** if you want others to access it.
> When creating a gist for the first time, it is often set to **private** by default.

To fetch the latest meal data from your Gist:

```
curl -H "Authorization: token YOUR_GIST_TOKEN" \
  https://api.github.com/gists/YOUR_GIST_ID
```

Or use the raw URL for the `meals.json` file in your Gist (public Gists only):

```
https://gist.githubusercontent.com/yourusername/YOUR_GIST_ID/raw/meals.json
```

> [!TIP]
> Checkout my live gist at [https://gist.github.com/samgutentag/62b60125077a9cb53ea81ba517262185](https://gist.github.com/samgutentag/62b60125077a9cb53ea81ba517262185)

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
- `GIST_TOKEN`: GitHub token with `gist` scope (required)
- `GIST_ID`: ID of the Gist to update (optional; if not set, a new Gist will be created)
