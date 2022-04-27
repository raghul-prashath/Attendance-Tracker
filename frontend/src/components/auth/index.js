import {createAuthProvider} from 'react-token-auth';    

export const {useAuth, authFetch, login, logout} = createAuthProvider({
        accessTokenKey: 'access_token',
        onUpdateToken: (token) => fetch('http://localhost:5000/refresh', {
            method: 'POST',
            body: token.access_token
        }).then(r => r.json())
    });

console.log(login)