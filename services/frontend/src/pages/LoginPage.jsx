import React from 'react';


const LoginPage = () => {


 const [username, setUsername] = React.useState('');
 const [password, setPassword] = React.useState('');
 const [response, setResponse] = React.useState("");

 const handleLogin =  () => {
    // Here you would typically make an API call to log in the user
    // For now, we will just log the username and password
    console.log("Username:", username);

 }

  return (
    <div>
        <div>
            <h2>Paw<span>Help</span></h2>
            <div>
                <input type="text" onChange= {(e) =>setUsername(e.target.value)}/>
                <input type="text" onChange= {(e) =>setUsername(e.target.value)}/>
            </div>
            <div>
                <button onClick={handleLogin} >
                    Login
                </button>
                <button onClick={() => alert('Register clicked')}>
                    Register
                </button>
            </div>
        </div>
    </div>

  )
}

export default LoginPage
