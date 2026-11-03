# PlaceReady (Pro) 🚀

A production-grade, full-stack AI-powered placement preparation platform designed to help students streamline and enhance their campus placement journey through intelligent resume analysis, personalized interview preparation, and structured learning roadmaps.

## ✨ Features

- **Modern User Experience:** An interactive and user-friendly web interface designed to provide a seamless placement preparation experience.
- **Secure Authentication:** JWT-based authentication with BCrypt password hashing to ensure secure user registration, login, and protected access.
- **AI-Powered Resume Analyzer:**
  - Supports multiple resume formats, including PDF and DOCX.
  - Automatically evaluates resumes using ATS scoring techniques.
  - Extracts relevant keywords, technical skills, and qualifications.
- **AI Mock Interview System:**
  - Dynamically generates placement interview questions based on user profiles and preparation needs.
  - Provides AI-driven answer evaluation, grading, and performance scoring.
  - Maintains historical interview records to track preparation progress.
- **Personalized Learning Roadmaps:** Generates structured placement preparation paths with organized topics and progress tracking to help students prepare systematically.

## 🛠️ Technology Stack (Python + AI)

- **Backend:** Python 3.11+, FastAPI
- **Database:** SQLite, Relational Database Management
- **AI Integration:** Anthropic Claude API for intelligent resume analysis, interview question generation, and response evaluation.
- **Authentication & Security:** PyJWT, BCrypt password hashing, JWT-based authorization
- **Server:** Uvicorn (ASGI Server)
- **Frontend:** HTML, CSS, JavaScript

## 🚀 Local Setup Instructions

1. **Create and navigate to the project directory:**

   ```bash
   cd placeready
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:** Create a `.env` file in the root directory and add your configurations:

   ```env
   ANTHROPIC_API_KEY=your_actual_anthropic_api_key
   JWT_SECRET=generate_a_long_random_secure_string
   CLAUDE_MODEL=claude-sonnet-5-5
   ```

5. **Run the Application:**

   ```bash
   uvicorn main:app --reload
   ```

   *The development server will start at `http://localhost:8000`.*

## 🛡️ Authentication & Security

PlaceReady (Pro) implements JWT-based authentication to secure user accounts and API endpoints. Passwords are protected using BCrypt hashing, while token verification ensures that only authenticated users can access protected resources. Environment variables are used to manage sensitive API credentials and security configurations.

## 📡 API Endpoints

- **Authentication**
  - `POST /auth/register` – Register a new user.
  - `POST /auth/login` – Authenticate users and generate access tokens.

- **Resume Operations**
  - `POST /resume/upload` – Upload and analyze resumes with ATS scoring.
  - `GET /resume/history` – Retrieve previous resume analysis records.

- **Interview Operations**
  - `POST /interview/generate` – Generate personalized mock interview questions.
  - `POST /interview/submit` – Submit answers for AI-based evaluation and scoring.

- **Roadmap Operations**
  - `/roadmap` – Access personalized placement preparation roadmaps.

## 🔮 Future Enhancements

- Real-time voice-based mock interviews with speech-to-text integration.
- Interactive peer-to-peer mock interview sessions.
- Automated GitHub portfolio analysis to evaluate projects and technical skills.
- AI-powered job and internship recommendations based on student profiles and skill sets.
