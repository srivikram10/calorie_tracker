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
├── app.py                   
├── database.sql              
├── calorie.db             
├── requirements.txt          
│
├── templates/                
│   └── index.html            
│
├── static/                   
│   ├── css/
│   │   └── style.css         
│   └── js/
│       └── script.js         
│
└── README.md                 # Project documentation


