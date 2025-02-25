import React from 'react'
import { useAPI } from './hooks/useAPI'

function App() {
  const { data, error, isLoading } = useAPI('/forecast')

  if (error) return <div>Failed to load forecast data</div>
  if (isLoading) return <div>Loading forecast...</div>

  return (
    <div>
      <h1>Swarmia Coding Exercise</h1>

      <p>Weather data:</p>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}

export default App 
