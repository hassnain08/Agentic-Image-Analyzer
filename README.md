# Agentic Image Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-v0.30+-blue)
![Gemini](https://img.shields.io/badge/Gemini-Vision-blueviolet)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)

> 🚀 Automatically analyze dashboard screenshots and generate insightful reports — no manual interpretation needed.

An Intelligent AI Agents crew that sees, understands, and explains by analyzing images and, transforms them into structured insights and detailed reports. No manual analysis needed.

Perfect for engineers, analysts, and executives who need fast, accurate summaries of dashboard data.
---

## 🧠 How It Works

1. **📸 Upload a Screenshot**  
   Provide a screenshot of a dashboard (e.g., energy monitoring, telecom analytics).

2. **🔍 AI Researcher Analyzes It**  
    `Image Data Researcher` agent:
   - Identifies charts, graphs, and UI elements
   - Extracts key metrics (e.g., load shedding hours, solar production, battery levels)
   - Summarizes 10 critical insights

3. **📄 Reporting Analyst Writes a Report**  
   The `Reporting Analyst` agent:
   - Turns insights into a structured, markdown-formatted report
   - Explains trends, anomalies, and patterns
   - Saves output to `report.md`

4. **📊 Get Actionable Intelligence**  
   Use the report for decision-making, sharing with teams, or integrating into workflows.

---

## 🛠️ Tech Stack

- **Framework**: [CrewAI](https://crewai.com) (multi-agent orchestration)
- **Vision Model**: Google Gemini Flash (multimodal vision-language)
- **Image Handling**: PIL, `google.generativeai`
- **Config**: YAML-based agents & tasks (clean, maintainable)
- **Output**: Markdown reports with optional CLI tools

---

Real-World Use Cases:
1. Energy Management
Monitor daily energy consumption, solar production, and battery usage
Detect anomalies (e.g., unexpected load shedding)
Generate daily summary reports for operations teams

2. Telecom Network Monitoring
Analyze network uptime, latency, data throughput
Automate field engineer reports from mobile app screenshots
Flag performance drops in real time

3. IoT & Smart Grids
Parse dashboards from SCADA systems or IoT platforms
Convert visual data into structured logs for further analysis

4. Executive Dashboards
Turn complex KPI dashboards into executive summaries
Enable non-technical leaders to understand technical data

5. Remote Site Diagnostics
Field technicians upload screenshots → get instant AI analysis
Reduce dependency on central engineers
