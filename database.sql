CREATE TABLE foods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,                     
    calories_per_100g REAL NOT NULL         
);


CREATE TABLE  daily_intake (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    food_id INTEGER NOT NULL,               
    quantity REAL NOT NULL,                 
    total_calories REAL NOT NULL,            
    intake_date DATE NOT NULL,               
    FOREIGN KEY (food_id) REFERENCES foods(id)
);


INSERT INTO foods (name, calories_per_100g) VALUES
('Rice', 130.0),
('Chicken', 239.0),
('Apple', 52.0),
('Banana', 89.0),
('Milk', 42.0),
('Egg', 155.0);
