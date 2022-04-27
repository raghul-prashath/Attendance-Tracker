import Login from './components/Login.js';
import Home from './components/Home.js';
import Test from './components/Test.js';

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Navigate
  } from "react-router-dom";


function App() {
    return (
        <div>
            <Router>
                <Routes>
                    <Route path="/" element = {<Login />}/>
                    <Route path="/Login" element = {<Login />}/>
                    <Route path="*" element={<Navigate replace to="/" />}/>
                    <Route path="/Home" element={<Home />}/>
                    <Route path="/Test" element={<Test />}/>
                </Routes>
            </Router>
        </div>
    );
};
  
export default App;
