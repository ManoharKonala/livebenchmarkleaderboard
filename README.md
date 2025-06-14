# 🤖 Tech Leaderboard Tracker

*Last updated: 2025-06-14 14:59 UTC*

This repository automatically tracks and displays the latest performance rankings for LLMs, IDEs, and AI Agents. The leaderboards are updated every 12 hours using GitHub Actions.

## 📊 LLM Leaderboard

| Rank | Model | Score | Organization | Type | Parameters |
|------|-------|-------|--------------|------|------------|
| 🥇 | **GPT-4 Turbo** | 87.3% | OpenAI | Commercial | 1.76T |
| 🥈 | **Claude-3.5 Sonnet** | 86.8% | Anthropic | Commercial | Unknown |
| 🥉 | **Gemini 1.5 Pro** | 85.9% | Google | Commercial | Unknown |
| 4 | **Llama 3.1 405B Instruct** | 84.7% | Meta | Open Source | 405B |
| 5 | **Qwen2.5 72B Instruct** | 83.5% | Alibaba | Open Source | 72B |
| 6 | **Mixtral 8x22B Instruct** | 82.1% | Mistral AI | Open Source | 141B |
| 7 | **Command R+** | 80.5% | Cohere | Commercial | 104B |
| 8 | **Llama 3.1 70B Instruct** | 79.8% | Meta | Open Source | 70B |
| 9 | **Yi-Large** | 78.9% | 01.AI | Commercial | Unknown |
| 10 | **DeepSeek-V2.5** | 77.8% | DeepSeek | Open Source | 236B |

## 🖥️ IDE Leaderboard

> **Note:** IDE data is sourced from the latest available Stack Overflow Developer Survey and is updated annually. It does **not** reflect real-time changes and only updates when a new survey is published.

| Rank | Name | Score | Organization | Type | Version |
|------|------|-------|--------------|------|---------|
| 🥇 | **Visual Studio Code** | 73.71 | Microsoft | Desktop | 1.90 |
| 🥈 | **Visual Studio** | 30.61 | Microsoft | Desktop | 2022 |
| 🥉 | **IntelliJ IDEA** | 29.11 | JetBrains | Desktop | 2024.1 |
| 4 | **Notepad++** | 24.21 | Notepad++ Team | Desktop | 8.6 |
| 5 | **Vim** | 22.21 | Bram Moolenaar | Desktop | 9.1 |
| 6 | **Sublime Text** | 20.71 | Sublime HQ | Desktop | 4 |
| 7 | **PyCharm** | 19.41 | JetBrains | Desktop | 2024.1 |
| 8 | **Eclipse** | 16.01 | Eclipse Foundation | Desktop | 2024-06 |
| 9 | **Xcode** | 12.91 | Apple | Desktop | 15.3 |
| 10 | **WebStorm** | 10.51 | JetBrains | Desktop | 2024.1 |

## 🤖 AI Agent Leaderboard

| Rank | Name | Score | Organization | Type | Version |
|------|------|-------|--------------|------|---------|
| 🥇 | **Auto-GPT** | 176132 | Significant-Gravitas | Open Source | None |
| 🥈 | **MetaGPT** | 56387 | geekan | Open Source | None |
| 🥉 | **AutoGen** | 45975 | microsoft | Open Source | None |
| 4 | **AgentGPT** | 34319 | reworkd | Web | None |
| 5 | **BabyAGI** | 21564 | yoheinakajima | Open Source | None |

## 📈 Key Statistics

- **LLMs Tracked**: 10
- **IDEs Tracked**: 10
- **AI Agents Tracked**: 5
- **Top LLM**: GPT-4 Turbo (87.3%)" if llms else ""
- **Top IDE**: Visual Studio Code (73.71)" if ides else ""
- **Top Agent**: Auto-GPT (176132)" if agents else ""

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

*Generated automatically by GitHub Actions*