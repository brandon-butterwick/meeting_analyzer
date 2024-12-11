import { useParams, Link } from 'react-router-dom'
import styled from '@emotion/styled'
import { agents } from '../data/agents'
import { useState } from 'react'

const AgentDetail = () => {
  const { id } = useParams()
  const agent = agents.find(a => a.id === id)
  const [input, setInput] = useState('')
  const [output, setOutput] = useState('')
  const [isProcessing, setIsProcessing] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!input.trim()) return

    setIsProcessing(true)
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1500))
      setOutput('Sample output for: ' + input)
    } catch (error) {
      setOutput('Error processing request')
    } finally {
      setIsProcessing(false)
    }
  }

  if (!agent) {
    return (
      <Container>
        <NotFound>
          <h2>Agent not found</h2>
          <Link to="/">Return to Home</Link>
        </NotFound>
      </Container>
    )
  }

  return (
    <Container>
      <Header>
        <IconWrapper>
          <img src={agent.icon} alt={agent.name} />
        </IconWrapper>
        <div>
          <h1>{agent.name}</h1>
          <p>{agent.description}</p>
          <Version>{agent.version}</Version>
        </div>
      </Header>

      <Content>
        <InputSection>
          <h2>Input</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Enter your input here..."
              disabled={isProcessing}
            />
            <button type="submit" disabled={isProcessing || !input.trim()}>
              {isProcessing ? 'Processing...' : 'Process'}
            </button>
          </form>
        </InputSection>

        <OutputSection>
          <h2>Output</h2>
          <div className="output-content">
            {isProcessing ? (
              <ProcessingMessage>Processing your request...</ProcessingMessage>
            ) : (
              output || 'Output will appear here...'
            )}
          </div>
        </OutputSection>
      </Content>
    </Container>
  )
}

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
`

const Header = styled.header`
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 2rem;
  background: var(--card-bg);
  border-radius: var(--border-radius);

  @media (max-width: 600px) {
    flex-direction: column;
    text-align: center;
  }
`

const IconWrapper = styled.div`
  width: 100px;
  height: 100px;
  background: var(--bg-color);
  border-radius: var(--border-radius);
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;

  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
`

const Version = styled.span`
  display: inline-block;
  background: var(--accent-color);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-top: 0.5rem;
`

const Content = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`

const InputSection = styled.section`
  h2 {
    margin-bottom: 1rem;
  }

  textarea {
    width: 100%;
    height: 200px;
    padding: 1rem;
    background: var(--card-bg);
    border: 1px solid var(--text-secondary);
    border-radius: var(--border-radius);
    color: var(--text-primary);
    resize: vertical;
    margin-bottom: 1rem;
    font-family: inherit;

    &:focus {
      outline: none;
      border-color: var(--accent-color);
    }

    &:disabled {
      opacity: 0.7;
      cursor: not-allowed;
    }
  }

  button {
    padding: 0.75rem 1.5rem;
    background: var(--accent-color);
    border: none;
    border-radius: var(--border-radius);
    color: white;
    cursor: pointer;
    font-size: 1rem;
    transition: opacity 0.2s;

    &:hover:not(:disabled) {
      opacity: 0.9;
    }

    &:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
  }
`

const OutputSection = styled.section`
  h2 {
    margin-bottom: 1rem;
  }

  .output-content {
    background: var(--card-bg);
    border-radius: var(--border-radius);
    padding: 1rem;
    min-height: 200px;
    white-space: pre-wrap;
    font-family: inherit;
  }
`

const ProcessingMessage = styled.div`
  color: var(--text-secondary);
  text-align: center;
  padding: 2rem;
`

const NotFound = styled.div`
  text-align: center;
  padding: 4rem 2rem;
  
  h2 {
    margin-bottom: 1rem;
  }

  a {
    color: var(--accent-color);
    text-decoration: none;
    
    &:hover {
      text-decoration: underline;
    }
  }
`

export default AgentDetail
