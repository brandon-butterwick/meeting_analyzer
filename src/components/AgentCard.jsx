import styled from '@emotion/styled'
import { Link } from 'react-router-dom'

const AgentCard = ({ agent }) => {
  return (
    <Link to={`/agent/${agent.id}`} style={{ textDecoration: 'none' }}>
      <Card>
        <ImageContainer>
          <IconWrapper>
            <img src={agent.icon} alt={`${agent.name} icon`} />
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
}

const Card = styled.div`
  background: var(--card-bg);
  border-radius: var(--border-radius);
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
  height: 100%;
  display: flex;
  flex-direction: column;
  cursor: pointer;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(9, 111, 160, 0.2);
  }
`

const ImageContainer = styled.div`
  position: relative;
  padding: 1.5rem;
  background: rgba(9, 111, 160, 0.05);
  display: flex;
  justify-content: center;
  align-items: center;
`

const IconWrapper = styled.div`
  width: 64px;
  height: 64px;
  background: var(--bg-color);
  border-radius: var(--border-radius);
  padding: 12px;
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
  flex: 1;
  display: flex;
  flex-direction: column;

  h2 {
    margin-bottom: 0.5rem;
    color: var(--text-primary);
    font-size: 1.25rem;
  }

  p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.4;
    flex: 1;
  }
`

export default AgentCard
