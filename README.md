# 🎫 Support Ticket Classification System

## 🚀 Overview

This project is a Machine Learning-based system that automatically classifies customer support tickets into categories and predicts their priority. It helps organizations streamline support workflows, reduce manual effort, and improve response time.

---

## 🎯 Key Features

* 📨 Classifies support tickets into categories
* ⚡ Predicts ticket priority (High / Medium / Low)
* 🧠 NLP-based text preprocessing and vectorization
* 🌐 Interactive web app using Streamlit
* 📊 Handles real-world customer support data

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **NLP:** TF-IDF Vectorizer
* **Models:**

  * Category Classification Model
  * Priority Prediction Model
* **Frontend:** Streamlit

---

## 📂 Project Structure

```text id="projstruct1"
support_ticket_classification/
│
├── streamlit_app.py              # Streamlit UI for predictions
├── customer_support_tickets.csv  # Dataset
├── ticket_model.ipynb            # Model training notebook
│
├── model/
│   ├── category_model.pkl        # Category prediction model
│   ├── priority_model.pkl        # Priority prediction model
│   └── vectorizer.pkl            # TF-IDF vectorizer
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters a support ticket description
2. Text is preprocessed (cleaning + TF-IDF vectorization)
3. Model predicts:

   * Ticket Category
   * Ticket Priority
4. Results are displayed instantly in the Streamlit app

---

## ▶️ How to Run the Project

### 1. Clone repository

```bash id="run1"
git clone https://github.com/your-username/support-ticket-classification.git
cd support-ticket-classification
```

### 2. Install dependencies

```bash id="run2"
pip install -r requirements.txt
```

### 3. Run the app

```bash id="run3"
streamlit run streamlit_app.py
```

---

## 📊 Example Use Cases

* Customer support automation
* Helpdesk ticket routing
* Priority-based issue handling
* IT service management

---

## 🧠 Future Enhancements

* 🔥 Use BERT / Deep Learning models
* 📊 Add sentiment-based priority detection
* 🌍 Deploy on cloud (AWS / Streamlit Cloud)
* 🔗 Integrate with real ticketing systems

---

## 👨‍💻 Author

**Harshal Suryawanshi**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
