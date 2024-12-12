import styled from '@emotion/styled'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <Nav>
      <Link to="/">
        <Logo>Agent Marketplace</Logo>
      </Link>
    </Nav>
  )
}

const Nav = styled.nav`
  background: var(--card-bg);
  padding: 1rem 2rem;
  margin-bottom: 2rem;

  a {
    text-decoration: none;
  }
`

const Logo = styled.h1`
  color: var(--text-primary);
  font-size: 1.5rem;
  margin: 0;
  
  &:hover {
    color: var(--accent-color);
  }
`

export default Navbar
