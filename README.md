# Startup Insure - A Django Web Project

Startup Insure is a responsive, multi-page website for a conceptual insurance company, built with Python and the Django web framework.

---

## Technology Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Database:** SQLite3 (for development)

---

## Features

* A clean, multi-page structure including Home, About, Services, and Contact pages.
* Uses Django's templating engine with a `base.html` for a consistent layout.
* Serves static assets (CSS) for styling.
* Organized project structure with a dedicated `pages` app.

---

## Setup and Run

### 1. Prerequisites
* Python 3.x
* Git

### 2. Installation
Clone the repository, set up a virtual environment, and install the required dependencies.

```bash
# Clone the repository
git clone [https://github.com/your-username/Startup_Insure.git](https://github.com/your-username/Startup_Insure.git)
cd Startup_Insure

# Create and activate a virtual environment
python -m venv Stup_env
# On Windows:
# .\\Stup_env\\Scripts\\activate
# On macOS/Linux:
# source Stup_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Application
Once the dependencies are installed, run the database migrations and start the development server.

```bash
# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### 4. View the Website
Open your web browser and navigate to **`http://127.0.0.1:8000`** to see the website.
