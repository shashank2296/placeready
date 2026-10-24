# PlaceReady (Pro) 🚀

A production-grade, full-stack AI placement preparation portal built with **FastAPI** and **SQLite**. Features JWT authentication, secure password hashing, dynamic resume analysis with ATS scoring, and automated AI interview generation.

## ✨ Features

* **Authentication & Security**

  * JWT-based authentication using `PyJWT`

  * BCrypt password hashing for secure credentials

  * Protected API endpoints via header token verification

* **Resume Analyzer**

  * Multi-format resume parsing (`PDF`, `DOCX`)

  * Automated ATS score calculation

  * Keyword and technical skills extraction

* **AI Mock Interviews**

  * Dynamic, tailored placement question generation

  * AI-driven response grading and scoring

  * Historical performance and interview tracking

* **Interactive Roadmaps**

  * Personal placement preparation paths

  * Structured progress tracking

## 🛠 Tech Stack

* **Backend Technology**

  * **Python 3.11+**: Primary programming language

  * **FastAPI**: Modern, high-performance web framework

  * **SQLite**: Lightweight relational database system

  * **Anthropic Claude API**: LLM core for resume analysis and question generation

  * **PyJWT**: Token-based security management

  * **BCrypt**: Safe password serialization

  * **Uvicorn**: ASGI web server implementation

## 📸 Screenshots

* **Auth Pages**: Sign In / Sign Up Interface

* **Core Dashboard**: Resume Upload & ATS Score Board, AI Interview Session Panel, Custom Study Roadmap

## 🚀 Getting Started

### Prerequisites

* Python 3.11+

* Anthropic API Key

### Environment Setup

Create a `.env` file in the root directory:

```
ANTHROPIC_API_KEY=your_actual_anthropic_api_key
JWT_SECRET=generate_a_long_random_secure_string
CLAUDE_MODEL=claude-sonnet-5-5

```

### Installation & Launch

Run the following commands in your terminal:

```
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload

```

The platform will be live at: `http://localhost:8000`

## 📁 Project Structure

```
placeready/
├── static/              # Frontend web interface (HTML, CSS, JS)
├── routes/              # FastAPI specialized routers
│   ├── auth.py          # Login, signup, and session controls
│   ├── resume.py        # Upload processing & ATS scoring
│   ├── interview.py     # Question generation & grading
│   └── roadmap.py       # Customized study maps
├── config.py            # Environment variables loader
├── database.py          # SQLite schema initialization & queries
├── main.py              # FastAPI app lifecycle definition
├── requirements.txt     # Back-end dependencies
└── .env                 # Local credentials configuration

```

## 🌐 Environment Variables

| Variable | Description | Default | 
| ----- | ----- | ----- | 
| `ANTHROPIC_API_KEY` | Key for Claude LLM integration | None (Required) | 
| `JWT_SECRET` | Signing token secret for sessions | `dev-secret-change-me` | 
| `CLAUDE_MODEL` | Anthropic model identifier | `claude-sonnet-5-5` | 

## 📡 API Endpoints

* **Authentication**

  * `POST /auth/register` - Create user profile

  * `POST /auth/login` - Authenticate user & receive token

* **Resume Operations**

  * `POST /resume/upload` - Parse resume & run ATS audit

  * `GET /resume/history` - Retrieve previously uploaded metrics

* **Interview Operations**

  * `POST /interview/generate` - Produce custom interview questions

  * `POST /interview/submit` - Grade and submit answer responses

## 🔮 Future Enhancements

* Audio voice-to-text integration for real-time oral interview prep

* Multi-user structural peer mock interview lobbies

* Automated GitHub portfolio scanners to match project structures

* Corporate vacancy application recommendation pipeline

## 📄 License

This project is licensed under the MIT License.