> Tags: Python, Flask, NLP, TextBlob, GingerIt, Web App, Grammar Correction, AI, Portfolio Project

# 📝 Grammar & Spell Checker (Flask + NLP)

A smart, web-based grammar and spelling correction tool built with **Python**, **Flask**, and NLP libraries like **TextBlob** and **Language-tool-python**. Designed to clean up user-entered or uploaded text with accurate grammar fixes and spelling suggestions.

---

## 🚀 Live Demo

🔗 [Try it now on Replit](https://replit.com/@yourusername/spell-checker-app)

---

## ✨ Features

- ✅ Context-aware **spelling correction** using TextBlob
- ✅ Rule-based **grammar suggestions** via GingerIt
- ✅ **Text box** input or **file upload** for flexibility
- ✅ Total issue count and correction list
- ✅ Clean, mobile-friendly UI with Bootstrap 5

---

## 🛠️ Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Backend       | Python, Flask       |
| NLP Libraries | TextBlob, Language-tool-python  |
| Frontend      | HTML, Bootstrap     |
| File Handling | Flask File Uploads  |

---

## 📸 Screenshots

> You can add these later once deployed.

| Text Input | Corrections |
|------------|-------------|
| ![input](screenshots/input.png) | ![output](screenshots/output.png) |

---

## 🔧 How to Run Locally

### Step 1: Clone this repository

```bash
git clone https://github.com/Rishita-rm/grammar-spell-checker-flask-nlp
cd grammar-spell-checker-flask-nlp
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### Step 3: Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```
spell-checker-app/
├── app.py                  # Flask app logic
├── Model.py                # Spell and grammar processing
├── requirements.txt
├── README.md
├── templates/
│   └── index.html          # Bootstrap UI
└── static/                 # Optional: add custom CSS or JS
```

---

## 📄 Sample Input

```
I like mashine learning and bananana.
```

### Output

- **Spelling**: `I like machine learning and banana.`
- **Grammar Corrections**:
  - `'mashine' → 'machine'`
  - `'bananana' → 'banana'`

---

## 🧠 What I Learned

- Working with Flask routing and templating
- Handling file uploads in Python
- Using NLP tools for spell and grammar analysis
- Parsing grammar suggestions from APIs
- Writing modular code for UI/backend separation

---

## 🚀 Future Improvements

- 🔍 Highlight corrections inline in the text
- 🌐 Multilingual support with translation tools
- 💾 Download corrected files
- 🔁 AJAX-based frontend (no reloads)
- 🧪 Add automated tests with pytest
- 🐳 Docker container for deployment

---

## 🙋 About Me

Hi! I'm a Python enthusiast passionate about building smart tools using NLP, AI, and web tech.

📫 [LinkedIn](https://www.linkedin.com/in/rishita-makkar-256851291/)    
🐍 [More Python Projects](https://github.com/Rishita-rm)

---

## 📜 License

MIT License – use it, improve it, share it!
