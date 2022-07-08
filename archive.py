# This is the "get it done in 10 minutes script"
#  I'll archive the other ladders later
import httpx

def build_url(region, leaderboard, season):
    return f"https://playhearthstone.com/en-us/community/leaderboards?region={region}&leaderboardId={leaderboard}&seasonId={str(season)}"

def archive(url):
    return httpx.get("https://web.archive.org/save/" + url)


if __name__ == '__main__':
    url = build_url("US", "WLD", 105)
    archive(url)
