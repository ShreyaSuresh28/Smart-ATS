# 📄 Smart ATS 2.0

An AI-powered Applicant Tracking System (ATS) built with Streamlit that helps recruiters analyze resumes, rank candidates, identify skill gaps, and generate feedback reports.

---

## 🚀 Features

### 👤 Candidate Module
- User Registration & Login
- Resume Upload (PDF)
- Secure Authentication
- Resume Storage

### 🧑‍💼 HR Module
- Job Description (JD) Input
- ATS Score Calculation
- Resume-JD Similarity Matching
- Candidate Ranking
- Skill Match Analysis
- Missing Skills Detection
- PDF Feedback Report Generation
- Downloadable Reports

### 📊 Analytics
- Candidate Ranking Table
- ATS Score Visualization
- Skill Gap Analysis
- Resume Screening Dashboard

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- SQLite

### Machine Learning & NLP
- Scikit-Learn
- TF-IDF Vectorization
- Cosine Similarity

### PDF Processing
- PyPDF2
- ReportLab

### Data Visualization
- Pandas
- Matplotlib

---

## 📂 Project Structure

```text
Smart_ATS_2.0/
│
├── database/
│   └── smart_ats.db
│
├── uploads/
│   └── Uploaded Resume PDFs
│
├── reports/
│   └── Generated ATS Reports
│
├── app.py
├── database.py
├── auth.py
├── matcher.py
├── resume_parser.py
├── feedback_generator.py
├── pdf_generator.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Smart_ATS_2.0.git
cd Smart_ATS_2.0
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📋 Workflow

### Candidate

1. Register Account
2. Login
3. Upload Resume
4. Resume stored in system

### HR

1. Login
2. Enter Job Description
3. Analyze Candidates
4. View ATS Scores
5. Download PDF Reports

---

## 📊 ATS Scoring Methodology

The system evaluates candidates using:

- TF-IDF Vectorization
- Cosine Similarity
- Skill Matching
- Missing Skill Detection

Final ATS Score is calculated based on resume relevance to the Job Description.

---

## 📄 Generated Reports

Each candidate receives:

- ATS Score
- Matched Skills
- Missing Skills
- Improvement Suggestions
- Downloadable PDF Report

---

## 🔒 Database Design

### Users Table

| Field | Type |
|---------|---------|
| id | INTEGER |
| username | TEXT |
| password | TEXT |
| role | TEXT |

### Resumes Table

| Field | Type |
|---------|---------|
| id | INTEGER |
| username | TEXT |
| email | TEXT |
| filename | TEXT |
| upload_date | TEXT |

### Feedback Table

| Field | Type |
|---------|---------|
| id | INTEGER |
| username | TEXT |
| score | REAL |
| matched_skills | TEXT |
| missing_skills | TEXT |
| report_path | TEXT |

---

## 🎯 Future Enhancements

- AI-Based Resume Suggestions
- Gemini/OpenAI Integration
- Resume Parsing using NLP
- Email Feedback Automation
- Admin Dashboard
- Multi-Role Authentication
- Resume Keyword Optimization
- Interview Question Generator

---

## 👩‍💻 Author

**Shreya K S**

BE - Computer Science & Engineering (AI & ML)

GitHub: https://github.com/ShreyaSuresh28

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
