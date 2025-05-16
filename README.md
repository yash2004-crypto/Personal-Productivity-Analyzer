# Personal-Productivity-Analyzer
A powerful Python-based personal productivity analysis tool that integrates calendar events, habit tracking data, and custom user inputs to generate insights and actionable feedback for better time management and habit building.

🚀 Features
📅 Integration with Google Calendar or .ics files to analyze event logs.

📈 Habit tracking data ingestion (CSV, Notion export, or manual input).

🧠 Insight generation: productive hours, focus trends, and time drains.

🔥 Visual reports using matplotlib and seaborn.

📤 Export options to PDF or Excel reports.

📊 Dashboard-ready datasets for Tableau or Power BI.

🧰 Technologies Used
Python 3.9+

pandas, numpy – Data manipulation

matplotlib, seaborn, plotly – Data visualization

google-api-python-client – Calendar API (optional)

openpyxl, fpdf – Reporting

sqlite3 – Local data storage (optional)

streamlit (optional) – Interactive frontend

📂 Project Structure
bash
Copy
Edit
personal-productivity-analyzer/
│
├── data/
│   ├── calendar_data.csv
│   ├── habits.csv
│
├── scripts/
│   ├── calendar_parser.py
│   ├── habit_analyzer.py
│   ├── productivity_report.py
│
├── dashboard/
│   ├── productivity_dashboard.twbx  # Tableau workbook
│
├── README.md
├── requirements.txt
└── main.py
⚙️ Setup Instructions
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/personal-productivity-analyzer.git
cd personal-productivity-analyzer
Create a Virtual Environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Prepare Your Data:

Add your calendar events in data/calendar_data.csv (start_time, end_time, event_type)

Add your habit tracking data in data/habits.csv (date, habit, status)

Run the Analyzer:

bash
Copy
Edit
python main.py
📤 Output
Summary statistics (total productive hours, top habits, etc.)

Time heatmaps & day-of-week analysis

Exported Excel or PDF reports

Tableau-ready datasets for dashboard creation

📈 Optional Dashboard (Power BI / Tableau)
Use the processed .csv or .xlsx output from the reporting module in your BI tool. Template dashboards are available in the dashboard/ folder.

🛠️ Customization
Modify the thresholds for productive time in config.py

Change color schemes in productivity_report.py

Add integrations for Notion, Toggl, or third-party APIs

🙌 Contributions
Pull requests and feedback are welcome! Please open an issue first to discuss changes.

📝 License
This project is licensed under the MIT License – see the LICENSE file for details.

