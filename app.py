from dotenv import load_dotenv
import os
import requests
from ics import Calendar
from datetime import datetime, timedelta
import json
import pytz

load_dotenv()

# Replace with your public Google Calendar .ics URL
ICAL_URL = os.getenv("ICAL_URL")
if not ICAL_URL:
    raise ValueError("ICAL_URL environment variable not set")


def get_current_week_dates():
    """Get the start and end dates for the current week (Monday to Sunday)"""
    today = datetime.now()
    # Calculate days since Monday (0 = Monday, 1 = Tuesday, etc.)
    days_since_monday = today.weekday()
    # Get Monday of current week
    monday = today - timedelta(days=days_since_monday)
    # Get Sunday of current week
    sunday = monday + timedelta(days=6)

    return monday.date(), sunday.date()


def convert_utc_to_local(utc_dt):
    """Convert UTC datetime to local time (PST/PDT)"""
    utc_tz = pytz.UTC
    local_tz = pytz.timezone("America/Los_Angeles")  # PST/PDT

    # Ensure the datetime is timezone-aware
    if utc_dt.tzinfo is None:
        utc_dt = utc_tz.localize(utc_dt)

    # Convert to local time
    local_dt = utc_dt.astimezone(local_tz)
    return local_dt


def closest_meal(hour):
    # Map exact hours to meal types
    meal_times = {8: "Breakfast", 11: "KidLunch", 12: "Lunch", 17: "Dinner"}
    return meal_times.get(hour, None)


def fetch_meals():
    print(f"Fetching calendar from: {ICAL_URL}")

    r = requests.get(ICAL_URL)

    # Check if the request was successful
    if r.status_code != 200:
        print(f"Error: HTTP {r.status_code}")
        print(f"Response content: {r.text[:500]}...")
        raise Exception(f"Failed to fetch calendar: HTTP {r.status_code}")

    # Check if the response is actually iCalendar data
    if not r.text.strip().startswith("BEGIN:VCALENDAR"):
        print("Error: Response is not valid iCalendar data")
        print(f"Response starts with: {r.text[:200]}...")
        raise Exception("Response is not valid iCalendar data")

    print("Successfully fetched iCalendar data")
    c = Calendar(r.text)

    meals_by_day = {}

    # Get current week dates
    week_start, week_end = get_current_week_dates()
    print(f"Filtering for current week: {week_start} to {week_end}")

    # Initialize all days in the current week with empty meal types
    current_date = week_start
    day_index = 0
    while current_date <= week_end:
        meals_by_day[day_index] = {
            "Breakfast": "",
            "KidLunch": "",
            "Lunch": "",
            "Dinner": "",
        }
        current_date += timedelta(days=1)
        day_index += 1

    for event in c.events:
        start_dt = event.begin.datetime

        # Convert UTC time to local time
        local_dt = convert_utc_to_local(start_dt)
        event_date = local_dt.date()

        # Only process events in the current week
        if week_start <= event_date <= week_end:
            # Calculate day index (0-6) for the current week
            days_since_monday = (event_date - week_start).days
            hour = local_dt.hour
            meal_type = closest_meal(hour)

            if meal_type:
                meals_by_day[days_since_monday][meal_type] = event.name

    return meals_by_day


if __name__ == "__main__":
    try:
        data = fetch_meals()
        # Sort the data by day index (0-6) to ensure proper order
        sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))
        with open("meals.json", "w") as f:
            json.dump(sorted_data, f, indent=2)
        print("Successfully processed meals and saved to meals.json")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
