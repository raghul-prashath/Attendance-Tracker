import './Login.css';
import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Cookies from 'universal-cookie';
 
const cookies = new Cookies();

const mode = 'login';
class LoginComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mode: this.props.mode
        }
    }
    toggleMode() {
        var newMode = this.state.mode === 'login' ? 'signup' : 'login';
        this.setState({ mode: newMode});
    }

    render() {
        return (
            <div>
                <div className={`form-block-wrapper form-block-wrapper--is-${this.state.mode}`} ></div>
                <section className={`form-block form-block--is-${this.state.mode}`}>
                    <header className="form-block__header">
                        <h1>{this.state.mode === 'login' ? 'Attendance Tracker' : 'Sign up'}</h1>
                        <div className="form-block__toggle-block">
                            <span>{this.state.mode === 'login' ? 'Don\'t' : 'Already'} have an account? Click here &#8594;</span>
                            <input id="form-toggler" type="checkbox" onClick={this.toggleMode.bind(this)} />
                            <label htmlFor="form-toggler"></label>
                        </div>
                    </header>
                    <LoginForm mode={this.state.mode} onSubmit={this.props.onSubmit}/>
                </section>
            </div>
        )
    }
}


class LoginForm extends React.Component {

    render() {
        return (
        <form onSubmit={this.props.onSubmit}>
            <div className="form-block__input-wrapper">
                <div className="form-group form-group--login">
                    <Input type="text" id="rollNoL" label="Rollno" disabled={this.props.mode === 'signup'}/>
                    <Input type="password" id="password" label="Password" disabled={this.props.mode === 'signup'}/>
                </div>
                <div className="form-group form-group--signup">
                    <Input type="text" id="rollNoR" label="Rollno" disabled={this.props.mode === 'login'} />
                    <Input type="text" id="name" label="Full name" disabled={this.props.mode === 'login'} />
                    <Input type="text" id="programme" label="Programme" disabled={this.props.mode === 'login'} />
                    <Input type="number" id="accYear" label="Academic year (in number)" disabled={this.props.mode === 'login'} />
                    <Input type="password" id="createpassword" label="Password" disabled={this.props.mode === 'login'} />
                </div>
            </div>
            <button className="button button--primary full-width" type="submit" >{this.props.mode === 'login' ? 'Log In' : 'Sign Up'}</button>
        </form>
        )
    }
}

const Input = ({ id, type, label, disabled }) => (
    <input className="form-group__input" type={type} id={id} placeholder={label} disabled={disabled} required/>
);



function Login() {

    let navigate = useNavigate();

    async function handleSubmit(event) {
        
        console.log('submit');
        event.preventDefault();   

        if(event.target[7].innerText === 'LOG IN'){
            const loginData = { "rollNo" : event.target[0].value, "password": event.target[1].value}
            
            axios.post("/api/users/login", loginData)
            .then(res => {
                if(res.status === 200){
                    sessionStorage.setItem("token", res.data.access_token)
                    cookies.set('access_token_cookie', res.data.access_token, { path: '/' }); 
                    navigate("Home");
                }

            })
        }
        else{
            const signupData = { "rollNo" : event.target[2].value, "name" : event.target[3].value, "programme" : event.target[4].value, "accYear" : event.target[5].value, "password" : event.target[6].value }
            console.log(signupData);
            axios.post("/api/users/register", signupData)
            .then(res => {
                if(res.status === 200){
                    sessionStorage.setItem("token", res.data.access_token)
                    cookies.set('access_token_cookie', res.data.access_token, { path: '/' }); 
                    navigate("Home");
                }
            })
        }
        
    }


    return (
        <div className={`app app--is-${mode}`}>
            <LoginComponent mode={mode} onSubmit={handleSubmit}/>
        </div>
    );
}

export default Login;