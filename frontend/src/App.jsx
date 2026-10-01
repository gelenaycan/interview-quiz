import { useState, useEffect } from "react"

function App() {
  const [data, setData] = useState(null)
  const [current, setCurrent] = useState(0)
  const [score, setScore] = useState(0)

  useEffect(() => {
    fetch("http://127.0.0.1:5001/questions")
      .then((response) => response.json())
      .then((result) => setData(result))
  }, [])

  function handleAnswer(option) {
    const question = data.questions[current]
    if (option === question.answer) {
      setScore(score + 1)
    }
    setCurrent(current + 1)
  }

  if (data === null) {
    return <p>Loading...</p>
  }

  if (current >= data.questions.length) {
    return (
      <div>
        <h1>Finished!</h1>
        <p>Your score: {score} / {data.questions.length}</p>
      </div>
    )
  }

  const question = data.questions[current]

  return (
    <div>
      <h1>Interview Prep Quiz</h1>
      <h2>{data.topic}</h2>
      <p>{data.lesson}</p>

      <h3>{question.question}</h3>
      {question.options.map((option) => (
        <button key={option} onClick={() => handleAnswer(option)}>
          {option}
        </button>
      ))}

      <p>Score: {score}</p>
    </div>
  )
}

export default App