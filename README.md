# Calorie Tracking Web Application

A web-based calorie tracking system developed using Python (Flask) and SQLite.  
The application helps users record daily food intake, monitor calorie limits, and visualize calorie consumption trends through interactive graphs.

---

## 📌 Features

- Limited food choices stored in a database
- Calories stored per 100 grams for each food item
- Daily food intake recording
- Automatic calorie calculation
- Graceful alerts when:
  - Daily calorie limit is exceeded
  - Daily calorie intake is below the limit
- Calorie trend visualization using line graphs:
  - Daily intake
  - Weekly intake
  - Monthly intake

---

## 🛠️ Technologies Used

- **Backend:** Python (Flask)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Charts:** Chart.js

---

## 🗂️ Project Structure

calorie-tracking-app/
│
├── app.py                    # Main Flask application
├── database.sql              # SQL script to create tables and insert food data
├── calorie.db               # SQLite database (auto-created)
├── requirements.txt          # Python dependencies
│
├── templates/                # HTML templates
│   └── index.html            # Main UI page
│
├── static/                   # Static assets
│   ├── css/
│   │   └── style.css         # Application styling
│   │
│   └── js/
│       └── script.js         # Frontend logic & Chart.js graphs
│
└── README.md                 # Project documentation

