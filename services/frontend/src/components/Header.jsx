
const Header = () =>{


  return (
  <header>
    <h1>A heading here</h1>
    <p>Posted by John Doe</p>
    <p>Some additional information here</p>
    <div>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/dashboard">Dashboard</a></li>
                <li><a href="/petsProfile">My Pets</a></li>
            </ul>
        </nav>
    </div>    
    <div>
        <div>
            <span className="iconImg"><a href="#"></a></span>
        </div>
        <div>
            User
        </div>
    </div>
  </header>

  )
}

export default Header
