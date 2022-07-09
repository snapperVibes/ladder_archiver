""" Archives the Hearthstone leaderboards using the Wayback Machine"""
import calendar
import time

import httpx
from datetime import date

regions = ["US", "API", "EU"]
modes = ["STD", "WLD", "CLS"]

def build_url(region, mode, season):
    return f"https://playhearthstone.com/en-us/community/leaderboards?region={region}&leaderboardId={mode}&seasonId={str(season)}"

def archive(url):
    return httpx.get("https://web.archive.org/save/" + url)

def months_since(x, y) -> int:
    year_diff = x.year - y.year
    month_diff = x.month - y.month
    return (year_diff * 12) + month_diff

def get_season(today):
    """ Returns the current Hearthstone season. """
    # Season 105 is during August 2022
    season_105 = date(year=2022, month=7, day=1)
    return months_since(today, season_105)

def main():
    today = date.today()
    season = get_season(today)

    # I'm too lazy to figure out timezones of when the season actually ends.
    # So on the first and last day of each month we will just record for both seasons
    first_day = date(today.year, today.month, 1)
    last_day = date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
    _potential_season = season
    if today == first_day:
        _potential_season = _potential_season -1
    elif today == last_day:
        _potential_season = _potential_season + 1

    seasons = {season, _potential_season}

    for region in regions:
        for mode in modes:
            for season in seasons:
                url = build_url(region, mode, season)
                archive(url)
                time.sleep(5)

if __name__ == '__main__':
    main()
