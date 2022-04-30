import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Cookies from 'universal-cookie';
 
const cookies = new Cookies();

function Logout() {

    let navigate = useNavigate();

    async function onClick(event) {
        event.preventDefault();   
        console.log("logout")

        axios.get("/api/users/logout", {withCredentials : true})
            .then(res => {
                console.log(res)
                if(res.status === 200){
                    cookies.remove('access_token_cookie', res.data.access_token, { path: '/' });
                    sessionStorage.removeItem('token');
                    navigate("Home");
                }
            })
    }
    const style = {
        marginLeft: 900,
        marginTop: -35

      };

    return (
        <div className="ml-72" style={style}>  
            <button onClick={onClick} className = "ml-72 font-bold text-white text-2xl place-items-end">Logout</button>
        </div>
    );
}

export default Logout;