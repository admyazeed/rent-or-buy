import { useEffect, useState } from 'react'
import './App.css'

const API_BASE = import.meta.env.VITE_API_URL;

function App() {
  const [questions, setQuestions] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState({})
  const [recommendation, setRecommendation] = useState(null)
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadQuestions = async () => {
      try {
        const response = await fetch(`${API_BASE}/questions`)

        if (!response.ok) {
          throw new Error('Unable to load questions right now.')
        }

        const data = await response.json()
        setQuestions(data)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    loadQuestions()
  }, [])

  const currentQuestion = questions[currentIndex]
  const progress = questions.length ? (Object.keys(answers).length / questions.length) * 100 : 0

  const handleSelect = (responseId) => {
    if (!currentQuestion) return

    setAnswers((previous) => ({
      ...previous,
      [currentQuestion.id]: responseId,
    }))
    setError('')
  }

  const handleNext = () => {
    if (!currentQuestion) return

    if (!answers[currentQuestion.id]) {
      setError('Please choose an answer before continuing.')
      return
    }

    if (currentIndex < questions.length - 1) {
      setCurrentIndex((index) => index + 1)
      return
    }

    submitAnswers()
  }

  const submitAnswers = async () => {
    if (questions.some((question) => !answers[question.id])) {
      setError('Please answer every question before seeing your result.')
      return
    }

    setSubmitting(true)
    setError('')

    try {
      const payload = {
        answers: questions.map((question) => ({
          question_id: question.id,
          response_id: answers[question.id],
        })),
      }

      const response = await fetch(`${API_BASE}/recommendation`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })

      if (!response.ok) {
        throw new Error('We could not calculate your recommendation.')
      }

      const result = await response.json()
      setRecommendation(result)
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  const handleRestart = () => {
    setAnswers({})
    setCurrentIndex(0)
    setRecommendation(null)
    setError('')
  }

  if (loading) {
    return (
      <main className="app-shell">
        <section className="card">
          <p className="eyebrow">Rent or Buy</p>
          <h1>Loading your questionnaire…</h1>
        </section>
      </main>
    )
  }

  if (recommendation) {
    return (
      <main className="app-shell">
        <section className="card results-card">
          <p className="eyebrow">Your result</p>
          <h1>{recommendation.recommendation}</h1>
          <p className="summary-text">
            Your recommendation is based on the responses you provided throughout the questionnaire. The factors below explain how each of your answers influenced the overall result, highlighting the considerations that most strongly support renting or buying in your current circumstances.
          </p>

          <div className="results-list">
            {questions.map((question) => {
              const selectedResponse = question.responses.find(
                (response) => response.id === answers[question.id],
              )

              return (
                <article className="summary-item" key={question.id}>
                  <h2>{question.text}</h2>
                  <p>
                    <strong>Your answer:</strong> {selectedResponse?.text}
                  </p>
                  <p>{selectedResponse?.explanation}</p>
                </article>
              )
            })}
          </div>

          <button type="button" className="secondary-button" onClick={handleRestart}>
            Start again
          </button>
        </section>
      </main>
    )
  }

  return (
    <main className="app-shell">
      <section className="card">
        <p className="eyebrow">Rent or Buy</p>
        <h1>Find the option that suits you best</h1>
        <p className="intro-text">
          Answer the following questions to receive a personalized recommendation on whether renting or buying may be a better fit for your current circumstances.
        </p>

        <div className="progress-bar" aria-label="Question progress">
          <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
        </div>

        <p className="progress-text">
          Question {currentIndex + 1} of {questions.length}
        </p>

        <div className="question-block">
          <h2>{currentQuestion.text}</h2>
          <div className="options-list">
            {currentQuestion.responses.map((response) => {
              const isSelected = answers[currentQuestion.id] === response.id

              return (
                <button
                  key={response.id}
                  type="button"
                  className={`option-button ${isSelected ? 'selected' : ''}`}
                  onClick={() => handleSelect(response.id)}
                >
                  {response.text}
                </button>
              )
            })}
          </div>
        </div>

        {error ? <p className="error-text">{error}</p> : null}

        <div className="actions">
          <button
            type="button"
            className="secondary-button"
            onClick={() => setCurrentIndex((index) => Math.max(index - 1, 0))}
            disabled={currentIndex === 0}
          >
            Back
          </button>
          <button type="button" className="primary-button" onClick={handleNext}>
            {submitting ? 'Working…' : currentIndex === questions.length - 1 ? 'See results' : 'Next'}
          </button>
        </div>
      </section>
    </main>
  )
}

export default App
