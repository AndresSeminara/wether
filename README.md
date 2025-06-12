# Weather Forecast App 🌦️
---

## 📦 Requirements

- Python 3.9+ (recommended)
- pip (Python package installer)
- A valid AccuWeather API key

---
## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone git@github.com:AndresSeminara/Weather.git
cd weather
```

2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---
## 🔐 Environment Variables

Create a .env file at the project root:

```code
API_KEY=your_accuweather_api_key
```

---
## 🚀 Running the Application

To start the main program:

```bash
python main.py
```

You will be prompted to enter a city name and receive a 5-day forecast summary.

---
## 🧪 Running Tests

To run the unit tests using pytest:

```bash
pytest
```