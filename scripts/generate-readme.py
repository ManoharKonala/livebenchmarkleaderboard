
#!/usr/bin/env python3
"""
README Generator for LLM Leaderboard
Generates a formatted README with the latest leaderboard data
"""

import json
from datetime import datetime
import os

def load_leaderboard_data():
    """Load leaderboard data from JSON file"""
    try:
        with open('data/leaderboard.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: leaderboard.json not found. Run scrape-leaderboard.py first.")
        return None

def generate_readme(data):
    """Generate README content with leaderboard data"""
    if not data or (not data.get('llms') and not data.get('ides') and not data.get('agents')):
        return None
    
    llms = data.get('llms', [])
    ides = data.get('ides', [])
    agents = data.get('agents', [])
    last_updated = data.get('last_updated', datetime.now().isoformat())

    # Format date
    try:
        update_date = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
        formatted_date = update_date.strftime("%Y-%m-%d %H:%M UTC")
    except:
        formatted_date = last_updated

    readme_content = f"""# 🤖 Tech Leaderboard Tracker

*Last updated: {formatted_date}*

This repository automatically tracks and displays the latest performance rankings for LLMs, IDEs, and AI Agents. The leaderboards are updated every 12 hours using GitHub Actions.

## 📊 LLM Leaderboard

| Rank | Model | Score | Organization | Type | Parameters |
|------|-------|-------|--------------|------|------------|
"""
    # LLM Leaderboard Table
    for entry in llms[:10]:
        rank_emoji = "🥇" if entry['rank'] == 1 else "🥈" if entry['rank'] == 2 else "🥉" if entry['rank'] == 3 else str(entry['rank'])
        readme_content += f"| {rank_emoji} | **{entry['model']}** | {entry['score']}% | {entry['organization']} | {entry.get('type', '')} | {entry.get('parameters', 'Unknown')} |\n"

    readme_content += f"""
## 🖥️ IDE Leaderboard

> **Note:** IDE data is sourced from the latest available Stack Overflow Developer Survey and is updated annually. It does **not** reflect real-time changes and only updates when a new survey is published.

| Rank | Name | Score | Organization | Type | Version |
|------|------|-------|--------------|------|---------|
"""
    # IDE Leaderboard Table
    for entry in ides[:10]:
        rank_emoji = "🥇" if entry['rank'] == 1 else "🥈" if entry['rank'] == 2 else "🥉" if entry['rank'] == 3 else str(entry['rank'])
        readme_content += f"| {rank_emoji} | **{entry['name']}** | {entry['score']} | {entry['organization']} | {entry.get('type', '')} | {entry.get('version', 'Unknown')} |\n"

    readme_content += f"""
## 🤖 AI Agent Leaderboard

| Rank | Name | Score | Organization | Type | Version |
|------|------|-------|--------------|------|---------|
"""
    # Agent Leaderboard Table
    for entry in agents[:10]:
        rank_emoji = "🥇" if entry['rank'] == 1 else "🥈" if entry['rank'] == 2 else "🥉" if entry['rank'] == 3 else str(entry['rank'])
        readme_content += f"| {rank_emoji} | **{entry['name']}** | {entry['score']} | {entry['organization']} | {entry.get('type', '')} | {entry.get('version', 'Unknown')} |\n"

    # Add overall stats section
    readme_content += f"""
## 📈 Key Statistics

- **LLMs Tracked**: {len(llms)}
- **IDEs Tracked**: {len(ides)}
- **AI Agents Tracked**: {len(agents)}
- **Top LLM**: {llms[0]['model']} ({llms[0]['score']}%)" if llms else ""
- **Top IDE**: {ides[0]['name']} ({ides[0]['score']})" if ides else ""
- **Top Agent**: {agents[0]['name']} ({agents[0]['score']})" if agents else ""

## 🔄 How This Works

This repository uses GitHub Actions to:
1. Run a scheduled workflow every 12 hours
2. Scrape the latest data for LLMs and AI Agents (real-time updates)
3. IDE rankings are updated annually from the latest Stack Overflow Developer Survey.
4. Generate an updated README and data file
5. Commit and push the changes automatically

## 📁 Repository Structure

```
├── .github/
│   └── workflows/
│       └── update-leaderboard.yml
├── scripts/
│   ├── scrape-leaderboard.py
│   └── generate-readme.py
├── data/
│   └── leaderboard.json
└── README.md
```

## 🛠️ Setup Instructions

1. Fork this repository
2. Enable GitHub Actions in your repository settings
3. The workflow will automatically start running every 12 hours

## 📊 Data Sources

- Hugging Face Open LLM Leaderboard
- Chatbot Arena by LMSYS
- Stack Overflow Developer Survey (for IDEs, annual update)
- Official AI Agent Repos/APIs

## 🤝 Contributing

Feel free to contribute by:
- Adding new data sources
- Improving the scraping logic
- Enhancing the README template
- Reporting issues or bugs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ Star this repository to stay updated with the latest rankings!

*Generated automatically by GitHub Actions*"""

    return readme_content

def main():
    print("Generating README...")
    
    # Load leaderboard data
    data = load_leaderboard_data()
    if not data:
        return
    
    # Generate README content
    readme_content = generate_readme(data)
    if not readme_content:
        print("Error: Could not generate README content")
        return
    
    # Write README file
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md updated successfully!")

if __name__ == "__main__":
    main()


