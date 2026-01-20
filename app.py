from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import date

app = Flask(__name__)

DATABASE = 'calorie.db'
DAILY_LIMIT = 2000

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    foods = conn.execute('SELECT * FROM foods').fetchall()
    conn.close()

    return render_template('index.html', foods=foods)


@app.route('/add', methods=['POST'])
def add_food():
    food_id = request.form['food_id']
    quantity = float(request.form['quantity'])
    today = date.today()
    conn = get_db()

    food = conn.execute(
        'SELECT calories_per_100g FROM foods WHERE id = ?',
        (food_id,)
    ).fetchone()

    total_calories = (food['calories_per_100g'] * quantity) / 100

    conn.execute(
        'INSERT INTO daily_intake VALUES (NULL, ?, ?, ?, ?)',
        (food_id, quantity, total_calories, today)
    )
    conn.commit()

    daily_total = conn.execute(
        'SELECT SUM(total_calories) FROM daily_intake WHERE intake_date = ?',
        (today,)
    ).fetchone()[0]

    conn.close()

    if daily_total > DAILY_LIMIT:
        msg = " Daily calorie limit exceeded!"
    else:
        msg = " You are below the daily calorie limit."

    return jsonify({"message": msg})

@app.route('/graph-data')
def graph_data():
    conn = get_db()

    daily = conn.execute("""
        SELECT intake_date, SUM(total_calories)
        FROM daily_intake
        GROUP BY intake_date
        ORDER BY intake_date
    """).fetchall()

    weekly = conn.execute("""
        SELECT strftime('%Y-%W', intake_date), SUM(total_calories)
        FROM daily_intake
        GROUP BY strftime('%Y-%W', intake_date)
        ORDER BY strftime('%Y-%W', intake_date)
    """).fetchall()


    monthly = conn.execute("""
        SELECT strftime('%Y-%m', intake_date), SUM(total_calories)
        FROM daily_intake
        GROUP BY strftime('%Y-%m', intake_date)
        ORDER BY strftime('%Y-%m', intake_date)
    """).fetchall()

    conn.close()

    daily = [[row[0], row[1]] for row in daily]
    weekly = [[row[0], row[1]] for row in weekly]
    monthly = [[row[0], row[1]] for row in monthly]

    return jsonify({
        "daily": daily,
        "weekly": weekly,
        "monthly": monthly
    })

if __name__ == '__main__':
    
    app.run(debug=True)