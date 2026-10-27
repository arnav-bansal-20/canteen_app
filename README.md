# 🍔 Cafeteria Compass

> **A Smart Campus Canteen & Nutrition-Aware Food Ordering Platform**

Cafeteria Compass is a modern web application built for university and school campuses. It bridges the gap between students, parents, and cafeteria staff by providing an intuitive food ordering system enriched with nutritional data, color-coded health indicators, and an AI-powered meal assistant powered by Google Gemini.

---

## ✨ Features

- **🥗 Dynamic Menu & Nutritional Transparency**
  - Over 150+ campus-ready menu items (Momos, Biryani, Rolls, Burgers, South/North Indian Meals, Beverages, and more).
  - Accurate breakdown of **Calories (kcal), Protein (P), Carbs (C), and Fats (F)** for every item.
  - **Color-Coded Health Choice Badges**:
    - 🟢 **Green Choice**: Nutrient-dense, balanced options.
    - 🟡 **Amber Choice**: Moderate nutritional profile.
    - 🔴 **Red Choice**: High-calorie, indulgence treats.

- **⚡ Fast Category Filters & Search**
  - Instant client-side filtering by categories: *Veg, Non-Veg, Beverages, Biryani, Burger, Chaat, Chinese, Combos, Dessert, Dosa, Maggi, Meals, Momo, Rolls, Snacks*, etc.
  - Full-text search for quick item lookup.

- **🛒 Interactive Cart & Ordering**
  - Slide-out order cart with live quantity adjustment and item totals.
  - Support for multiple order modes (**Place Order** & **Vend Receipt**).

- **🤖 AI Canteen Assistant (Gemini-Powered)**
  - Floating campus chatbot providing personalized recommendations based on student budget and preferences.
  - Calculates a **Health Score (1-10)** for suggested meals and weekly meal plans.
  - Enforces strict menu adherence and nutrition reporting.

- **👥 Role-Based Portals**
  - **Student**: Browse menu, build cart, place orders, chat with AI, and review meals.
  - **Parent**: Monitor order history and meal choices for student health tracking.
  - **Teacher**: Fast campus ordering.

- **⭐ Community Reviews & Ratings**
  - Authentic student ratings and reviews for dishes across the canteen.

- **🛠️ CLI & Management Utilities**
  - `view_db.py`: CLI tool for pretty-printing database users, orders, and recent reviews.
  - `seed_data.py`: Populates the menu with 156 items and simulated reviews.
  - `setup_db.py`: Initializes the database and executes the schema.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, Jinja2, Werkzeug
- **Database**: MySQL, `mysql-connector-python`
- **AI / LLM**: Google Gemini API (`google-generativeai`)
- **Frontend**: Responsive HTML5, CSS3, Vanilla JavaScript, FontAwesome
- **Configuration**: `python-dotenv`

---

## 📁 Project Structure

```text
canteen_app/
├── app.py              # Main Flask application & API routes
├── db.py               # Resilient MySQL connection handler
├── schema.sql          # Database table definitions
├── setup_db.py         # Automated database & schema initialization
├── seed_data.py        # Seeds 156 menu items and reviews
├── view_db.py          # Terminal CLI viewer for database records
├── requirements.txt    # Python package dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore specifications
├── static/
│   ├── css/
│   │   └── style.css   # Modern cafeteria design system
│   └── js/
│       └── main.js     # Client-side cart and interaction logic
└── templates/
    ├── base.html       # Base layout, navbar, search & floating AI bot
    ├── menu.html       # Filterable food menu grid
    ├── cart.html       # Cart view
    ├── history.html    # Order history & receipts
    ├── login.html      # Authentication portal
    └── register.html   # Account registration
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- MySQL Server (running locally or remotely)
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/arnav-bansal-20/canteen_app.git
cd canteen_app
```

### 3. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
Open `.env` and fill in your values:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_SECRET_KEY=your_secret_key_here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=canteen_db
PORT=5001
```

### 6. Initialize & Seed Database
Make sure your MySQL server is running, then run:
```bash
# 1. Create database and tables
python setup_db.py

# 2. Seed 156 menu items and reviews
python seed_data.py
```

You can view the seeded database directly in your terminal anytime with:
```bash
python view_db.py
```

### 7. Run the Application
```bash
python app.py
```
Open your browser and navigate to:
**[http://127.0.0.1:5001](http://127.0.0.1:5001)**

---

## 🔑 Default Test Accounts

| Role | Username | Password |
|---|---|---|
| **Student** | `student` or `arnav` | `password123` |
| **Parent** | `parent` | `password123` |
| **Teacher** | `teacher` | `password123` |

You can also register a new account on the registration page.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
