import os
import requests
import json
import argparse
from dotenv import load_dotenv

from templates.header import get_header_svg
from templates.typing import get_typing_svg
from templates.stats import get_stats_card_svg
from templates.languages import get_languages_svg
from templates.matrix import get_matrix_svg
from templates.scanner import get_scanner_svg
from templates.wave import get_wave_svg
from templates.activity import get_activity_graph_svg
from templates.terminal import get_terminal_svg
from templates.focus import get_focus_svg
from templates.badge import get_contact_badge_svg

load_dotenv()

GITHUB_TOKEN = (os.getenv("METRICS_TOKEN") or os.getenv("GITHUB_TOKEN") or "").strip()

def fetch_data(username):
    query = """
    query($login: String!) {
      user(login: $login) {
        login
        name
        repositories(first: 100, ownerAffiliations: OWNER, orderBy: {field: STARGAZERS, direction: DESC}) {
          nodes {
            stargazerCount
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node { name }
              }
            }
          }
        }
        contributionsCollection {
          totalCommitContributions
          totalPullRequestContributions
          totalIssueContributions
          restrictedContributionsCount
          contributionCalendar {
            weeks {
              contributionDays {
                contributionCount
                color
                date
              }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.post("https://api.github.com/graphql", json={"query": query, "variables": {"login": username}}, headers=headers)
    if response.status_code != 200: raise Exception(f"Query failed: {response.text}")
    res_data = response.json()
    if "errors" in res_data: raise Exception(f"GraphQL errors: {res_data['errors']}")
    
    data = res_data["data"]["user"]
    total_stars = sum(repo["stargazerCount"] for repo in data["repositories"]["nodes"])
    commits = data["contributionsCollection"]["totalCommitContributions"] + data["contributionsCollection"]["restrictedContributionsCount"]
    lang_stats = {}
    for repo in data["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            lang_stats[name] = lang_stats.get(name, 0) + edge["size"]
    total_size = sum(lang_stats.values())
    languages = sorted([(k, round(v/total_size*100, 1)) for k,v in lang_stats.items()], key=lambda x: x[1], reverse=True)
    return {
        "username": data["login"], "stars": total_stars, "commits": commits,
        "prs": data["contributionsCollection"]["totalPullRequestContributions"],
        "issues": data["contributionsCollection"]["totalIssueContributions"],
        "languages": languages, "calendar": data["contributionsCollection"]["contributionCalendar"]["weeks"]
    }

def main():
    parser = argparse.ArgumentParser(description="GitHub Metrics SVG Generator")
    parser.add_argument("--username", type=str, default="blackalex1", help="GitHub username")
    parser.add_argument("--telegram", type=str, help="Telegram username (optional, defaults to github username)")
    parser.add_argument("--color", type=str, default="#00FFAA", help="Primary accent color (hex)")
    parser.add_argument("--graphs", type=str, nargs="+", default=["all"], help="Specific graphs to generate (header, stats, languages, typing, matrix, scanner, wave, activity, terminal, focus, telegram)")
    
    args = parser.parse_args()
    
    if not GITHUB_TOKEN:
        print("Error: METRICS_TOKEN or GITHUB_TOKEN not found in environment.")
        return
        
    try:
        print(f"Fetching data for {args.username}...")
        data = fetch_data(args.username)
        print("Generating SVGs...")
        os.makedirs("output", exist_ok=True)
        
        target_graphs = args.graphs
        if "all" in target_graphs:
            target_graphs = ["header", "stats", "languages", "typing", "matrix", "scanner", "wave", "activity", "terminal", "focus", "telegram"]

        if "header" in target_graphs:
            with open("output/header.svg", "w", encoding="utf-8") as f:
                f.write(get_header_svg(data["username"], "Infosec Researcher | Reverse Engineer"))
        
        if "stats" in target_graphs:
            with open("output/stats.svg", "w", encoding="utf-8") as f:
                f.write(get_stats_card_svg(data, color=args.color))
        
        if "languages" in target_graphs:
            with open("output/languages.svg", "w", encoding="utf-8") as f:
                f.write(get_languages_svg(data["languages"], color=args.color))
        
        if "typing" in target_graphs:
            with open("output/typing.svg", "w", encoding="utf-8") as f:
                f.write(get_typing_svg(["whoami;", "infosec researcher;", "reverse engineering;", "pentesting;"], color=args.color))
        
        if "matrix" in target_graphs:
            with open("output/matrix.svg", "w", encoding="utf-8") as f:
                f.write(get_matrix_svg(data["calendar"], color=args.color))
        
        if "scanner" in target_graphs:
            with open("output/scanner.svg", "w", encoding="utf-8") as f:
                f.write(get_scanner_svg(data["calendar"], color=args.color))
        
        if "wave" in target_graphs:
            with open("output/wave.svg", "w", encoding="utf-8") as f:
                f.write(get_wave_svg(data["calendar"], color=args.color))
        
        if "activity" in target_graphs:
            with open("output/activity.svg", "w", encoding="utf-8") as f:
                f.write(get_activity_graph_svg(data["calendar"], color=args.color))
            
        if "terminal" in target_graphs:
            terminal_data = {
                "role": "Infosec Researcher / RE",
                "focus": "Cybersecurity | C/C++ | Networking",
                "system": "Linux / Windows Internals",
                "mindset": "\"Break to understand. Build better.\""
            }
            with open("output/terminal.svg", "w", encoding="utf-8") as f:
                f.write(get_terminal_svg(terminal_data, color=args.color))
            
        if "focus" in target_graphs:
            with open("output/focus.svg", "w", encoding="utf-8") as f:
                f.write(get_focus_svg(color=args.color))
            
        if "telegram" in target_graphs:
            with open("output/telegram.svg", "w", encoding="utf-8") as f:
                tg_handle = args.telegram if args.telegram else args.username
                f.write(get_contact_badge_svg(username=tg_handle, color=args.color))
            
        print(f"Successfully generated {len(target_graphs)} SVGs in 'output/' directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
