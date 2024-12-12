import { useParams, Link } from 'react-router-dom'
import styled from '@emotion/styled'
import { agents } from '../data/agents'
import { useState } from 'react'

const AgentDetail = () => {
  const { id } = useParams()
  const agent = agents.find(a => a.id === id)
  const [files, setFiles] = useState({
    transcript: null,
    background: null,
    roles: null,
    timeline: null,
    prep: null
  })
  const [output, setOutput] = useState('')
  const [isProcessing, setIsProcessing] = useState(false)

  if (!agent) {
    return (
      <Container>
        <div>Agent not found. <Link to="/">Return home</Link></div>
      </Container>
    )
  }

  const handleFileChange = (type, e) => {
    const file = e.target.files[0]
    if (file && file.type === 'application/pdf') {
      setFiles(prev => ({ ...prev, [type]: file }))
    } else {
      alert('Please upload a PDF file')
      e.target.value = ''
    }
  }

  const getRandomProcessingTime = () => {
    const mean = 3000
    const stdDev = 500
    let time = mean + (stdDev * (Math.random() + Math.random() + Math.random() - 1.5))
    return Math.min(Math.max(time, 2000), 4500)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!Object.values(files).every(file => file)) {
      alert('Please upload all required PDF files')
      return
    }

    setIsProcessing(true)
    setOutput('')

    const processingTime = getRandomProcessingTime()
    
    setTimeout(() => {
      const analysisText = `**Meeting Analysis**

**Date:** Not specified
**Time:** Not specified
**Attendees:** Brandon Butterwick and Nick Kerr
**Duration:** Approximately 12 minutes (based on the number of pauses between utterances)

**Purpose:**
The meeting appears to be a discussion between Brandon, who is taking on a new role related to the "first day experience" for new employees, and Nick, who is knowledgeable about the current process for setting up new computers and helping remote users. The purpose of the meeting was for Brandon to ask questions and gather information from Nick to aid in his new role.

**Discussion Points:**

1. **Computer setup process:** Brandon asked about the process for setting up new computers for employees, including how to ensure that the computer is available at the office if the employee requests it.
2. **Support for remote users:** Nick mentioned an optional support system for remote users who can contact a team member (Livia) via phone or video call for assistance with setting up their computer.
3. **Opal's role:** Brandon informed Nick that he would be working with Opal, the new person responsible for overseeing the first day experience for new employees.
4. **Brandon's role and job responsibilities:** Brandon mentioned that he has a new title but is still figuring out his specific job responsibilities.
5. **Personal updates:** The two attendees also discussed their personal lives, including Brandon's recent move to California.

**Key Takeaways:**

1. Brandon will be taking on a new role related to the "first day experience" for new employees.
2. Nick provided information about the current process for setting up new computers and supporting remote users.
3. Opal is the new person responsible for overseeing the first day experience for new employees.

**Action Items:**

1. Brandon will work with Opal to implement changes related to the first day experience.
2. Brandon will continue to learn more about his role and job responsibilities.
3. Nick will likely be a resource for Brandon as he takes on his new role.`

      setOutput(analysisText)
      setIsProcessing(false)
    }, processingTime)
  }

  return (
    <Container>
      <Header>
        <img src={agent.icon} alt={agent.name} />
        <div>
          <h1>{agent.name}</h1>
          <p>{agent.description}</p>
          <Version>{agent.version}</Version>
        </div>
      </Header>

      <Content>
        <Form onSubmit={handleSubmit}>
          <UploadSection>
            <UploadField>
              <label>Meeting Transcript</label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => handleFileChange('transcript', e)}
                disabled={isProcessing}
              />
            </UploadField>

            <UploadField>
              <label>Project Background</label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => handleFileChange('background', e)}
                disabled={isProcessing}
              />
            </UploadField>

            <UploadField>
              <label>Team Roles</label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => handleFileChange('roles', e)}
                disabled={isProcessing}
              />
            </UploadField>

            <UploadField>
              <label>Project Timeline</label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => handleFileChange('timeline', e)}
                disabled={isProcessing}
              />
            </UploadField>

            <UploadField>
              <label>Meeting Preparation & Agenda</label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => handleFileChange('prep', e)}
                disabled={isProcessing}
              />
            </UploadField>

            <Button type="submit" disabled={isProcessing}>
              {isProcessing ? 'Processing...' : 'Process Files'}
            </Button>
          </UploadSection>
        </Form>

        <OutputSection>
          <h2>Output</h2>
          <OutputContent>
            <pre>{output || 'Output will appear here...'}</pre>
          </OutputContent>
        </OutputSection>
      </Content>
    </Container>
  )
}

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
`

const Header = styled.header`
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 2rem;
  background: var(--card-bg);
  border-radius: var(--border-radius);

  img {
    width: 100px;
    height: 100px;
    border-radius: var(--border-radius);
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

const Form = styled.form`
  background: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 1.5rem;
`

const UploadSection = styled.div`
  display: grid;
  gap: 1.5rem;
`

const UploadField = styled.div`
  label {
    display: block;
    margin-bottom: 0.5rem;
  }

  input {
    width: 100%;
    padding: 0.5rem;
    background: var(--bg-color);
    border: 1px solid var(--text-secondary);
    border-radius: var(--border-radius);
    color: var(--text-primary);
  }
`

const Button = styled.button`
  width: 100%;
  padding: 1rem;
  background: var(--accent-color);
  border: none;
  border-radius: var(--border-radius);
  color: white;
  cursor: pointer;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`

const OutputSection = styled.div`
  h2 {
    margin-bottom: 1rem;
  }
`

const OutputContent = styled.div`
  background: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  min-height: 200px;
  
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
    font-family: monospace;
    color: var(--text-primary);
  }
`

export default AgentDetail
