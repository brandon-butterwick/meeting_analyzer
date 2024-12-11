import styled from '@emotion/styled'
import AgentCard from '../components/AgentCard'
import { agents } from '../data/agents'
import { useState } from 'react'

const Home = () => {
  const [searchQuery, setSearchQuery] = useState('')

  const filteredAgents = agents.filter(agent => 
    agent.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    agent.description.toLowerCase().includes(searchQuery.toLowerCase())
  )

  return (
    <Container>
      <Header>
        <h1>Discover AI Agents</h1>
        <SearchInput 
          type="text" 
          placeholder="Search agents..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </Header>
      <Grid>
        {filteredAgents.map(agent => (
          <AgentCard key={agent.id} agent={agent} />
        ))}
        {filteredAgents.length === 0 && (
          <NoResults>No agents found matching your search.</NoResults>
        )}
      </Grid>
    </Container>
  )
}

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
`

const Header = styled.header`
  margin-bottom: 2rem;
  
  h1 {
    margin-bottom: 1rem;
    font-size: 2rem;
  }
`

const SearchInput = styled.input`
  width: 100%;
  padding: 1rem;
  border-radius: var(--border-radius);
  border: 1px solid var(--text-secondary);
  background: var(--card-bg);
  color: var(--text-primary);
  font-size: 1rem;

  &:focus {
    outline: none;
    border-color: var(--accent-color);
  }
`

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  padding-bottom: 2rem;
`

const NoResults = styled.div`
  grid-column: 1 / -1;
  text-align: center;
  padding: 2rem;
  color: var(--text-secondary);
`

export default Home
