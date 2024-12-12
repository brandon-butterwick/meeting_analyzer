import styled from '@emotion/styled'
import { Link } from 'react-router-dom'

const AgentCard = ({ agent }) => (
  <Link to={`/agent/${agent.id}`} style={{ textDecoration: 'none' }}>
    <Card>
      <ImageContainer>
        <IconWrapper>
          <img src={agent.icon} alt={agent.name} />
        </IconWrapper>
        <Version>{agent.version}</Version>
      </ImageContainer>
      <Content>
        <h2>{agent.name}</h2>
        <p>{agent.description}</p>
      </Content>
    </Card>
  </Link>
)

const Card = styled.div`
  background: var(--card-bg);
  border-radius: var(--border-radius);
  overflow: hidden;
  transition: transform 0.2s;
  cursor: pointer;

  &:hover {
    transform: translateY(-4px);
  }
`

const ImageContainer = styled.div`
  position: relative;
  padding: 1.5rem;
  background: rgba(9, 111, 160, 0.05);
  display: flex;
  justify-content: center;
`

const IconWrapper = styled.div`
  width: 64px;
  height: 64px;
  background: var(--bg-color);
  border-radius: var(--border-radius);
  padding: 12px;

  img {
    width: 100%;
    height: 100%;
  }
`

const Version = styled.span`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: var(--accent-color);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  color: white;
`

const Content = styled.div`
  padding: 1.5rem;

  h2 {
    margin-bottom: 0.5rem;
    color: var(--text-primary);
  }

  p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.4;
  }
`

export default AgentCard
