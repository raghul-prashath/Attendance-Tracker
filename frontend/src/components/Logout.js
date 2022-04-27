import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import {logout} from "./auth";

function Logout() {

    let navigate = useNavigate();

    async function onClick(event) {
        event.preventDefault();   
        console.log("logout")
        axios.post(`http://localhost:5000/users/logout`, {})
            .then(res => {
                if(res.status === 200){
                    logout();
                    navigate("Home", {state : {auth : false}});
                }

            })
    }

    return (
        <div>
            
            <button onClick={onClick} className = "mt-12 ml-12 content-end font-bold text-white text-2xl">Logout</button>
            
        </div>
    );
}

export default Logout;