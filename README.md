# Rent or Buy

Rent or Buy is a small full-stack questionnaire that helps someone think through whether renting or buying a home may better fit their current circumstances. It is designed as a portfolio project demonstrating a React frontend, a FastAPI backend, typed request/response models, and a focused recommendation service.

The app asks 10 questions about factors such as length of stay, income stability, savings, and mobility. Each answer contributes a positive or negative weight. The final result includes the recommendation, total score, and an explanation for each answer.

## Features

- Step-by-step questionnaire with progress tracking
- Required-answer validation before moving forward or submitting
- Buy, Rent, or Either recommendation based on a transparent weighted score
- Result breakdown showing the selected answer and its rationale
- Restart flow for trying a different set of answers
- FastAPI endpoints that can be used independently of the React UI
- Automated backend tests for API behavior and recommendation rules

## Technology

- **Frontend:** React 19, Vite, JavaScript, CSS
- **Backend:** Python, FastAPI, Pydantic
- **Testing:** pytest, FastAPI `TestClient`

## Project Structure

```text
backend/
	app/
		data/questions.py                 Questionnaire content and weights
		models/                           Pydantic request/response models
		routers/questionnaire.py          API routes
		services/recommendation_engine.py Scoring and recommendation rules
		tests/                            Backend tests
frontend/
	src/App.jsx                         Questionnaire UI and API calls
	src/App.css                         Component styles
	package.json                        Frontend scripts and dependencies
```

## Run Locally

You will need Python 3.10 or newer and Node.js 18 or newer.

### 1. Start the backend

From the repository root, create and activate a virtual environment, then install the Python dependencies:

```bash
cd backend
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8000`. Interactive API documentation is available at `http://localhost:8000/docs`.

### 2. Start the frontend

In a second terminal:

```bash
cd frontend
npm install
```

Create `frontend/.env.local` with the backend URL:

```env
VITE_API_URL=http://localhost:8000
```

Start the Vite development server:

```bash
npm run dev
```

Open the URL printed by Vite, normally `http://localhost:5173`.

## Tests and Checks

Run the backend tests from the `backend` directory while the virtual environment is active:

```bash
pytest
```

Run the frontend lint and production build from the `frontend` directory:

```bash
npm run lint
npm run build
```

## API

### `GET /questions`

Returns the 10-question questionnaire. Each question contains response options with their scoring weights and explanations.

### `POST /recommendation`

Accepts one selected response for each question:

```json
{
	"answers": [
		{"question_id": 1, "response_id": 4},
		{"question_id": 2, "response_id": 3}
	]
}
```

The response includes the total score and the recommendation:

```json
{
	"recommendation": "Either",
	"score": 2,
	"factors": [
		{
			"category": "Length of Stay",
			"weight": 3,
			"explanation": "..."
		}
	]
}
```

The current rule is:

- Score `10` or higher: **Buy**
- Score `-10` or lower: **Rent**
- Otherwise: **Either**