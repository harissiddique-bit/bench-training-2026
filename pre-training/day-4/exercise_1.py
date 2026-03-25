import sys
import requests

BASE_URL = "https://api.github.com/users"


def fetch_user(username):
    url = f"{BASE_URL}/{username}"
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print("User not found.")
            return None
        elif response.status_code == 403:
            print("Rate limit exceeded. Try again later.")
            return None
        elif response.status_code != 200:
            print(f"Unexpected error: {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")
        return None


def fetch_repos(username):
    url = f"{BASE_URL}/{username}/repos"
    try:
        response = requests.get(url)

        if response.status_code != 200:
            return []

        return response.json()

    except requests.exceptions.RequestException:
        return []


def get_top_repos(repos, top_n=5):
    sorted_repos = sorted(
        repos,
        key=lambda x: x.get("stargazers_count", 0),
        reverse=True
    )
    return sorted_repos[:top_n]


def display_profile(user_data, top_repos):
    print("\n=== GitHub Profile ===")
    print(f"Username       : {user_data.get('login')}")
    print(f"Bio            : {user_data.get('bio')}")
    print(f"Public Repos   : {user_data.get('public_repos')}")
    print(f"Followers      : {user_data.get('followers')}")

    print("\n=== Top Repositories ===")
    if not top_repos:
        print("No repositories found.")
        return

    for repo in top_repos:
        print(
            f"- {repo.get('name') or 'N/A':<10} | {repo.get('stargazers_count') or 'N/A':<10} | {repo.get('language') or 'N/A':<10}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 exercise_1.py <github_username>")
        return

    print(sys.argv)
    username = sys.argv[1]

    user_data = fetch_user(username)
    if not user_data:
        return

    repos = fetch_repos(username)
    top_repos = get_top_repos(repos)

    display_profile(user_data, top_repos)



main()
