import React from 'react';
import { useSpring, animated} from 'react-spring';
import './Home.css';
import Logout from './Logout.js';

const attendanceData = [
    {
      id: 1,
      name: "18XD81 Reinforcement Learning",
      transactions: 75,
      rise: false,
      tasksCompleted: 5,
      classCompleted: 5,
    },
  
    {
      id: 2,
      name: "18XD82 NLP",
      transactions: 59,
      rise: false,
      tasksCompleted: 5,
      classCompleted: 15,
    },
  
    {
      id: 3,
      name: "18XD83 Cloud Computing",
      transactions: 60,
      rise: true,
      tasksCompleted: 1,
      classCompleted: 25,
    },
    {
      id: 4,
      name: "18XD85 Reinforcement Learning Lab",
      transactions: 26,
      rise: true,
      tasksCompleted: 1,
      classCompleted: 25,
    }
  ];
  
function Content() {
    return React.createElement("div",{ className: "flex w-full" },
        React.createElement("div", {className:" h-screen flex-grow overflow-x-hidden overflow-auto flex flex-wrap content-start p-8"},
            attendanceData.map(({id, name, position, transactions, rise, tasksCompleted, classCompleted }) =>
            React.createElement(NameCard, {
                key: id,
                id: id,
                name: name,
                position: position,
                transactionAmount: transactions,
                rise: rise,
                tasksCompleted: tasksCompleted,
                classCompleted: classCompleted
            })) 
        )
    );
}
  
function NameCard({
    name,
    transactionAmount,
    rise,
    tasksCompleted,
    classCompleted,
    }) {
    const { barPlayhead } = useSpring({
        barPlayhead: 1,
        from: { barPlayhead: 0 }
    });


    return( React.createElement("div",{
        className: "w-full p-2 lg:w-1/3" }, 
        
        React.createElement("div", { className: "rounded-lg bg-card flex justify-between p-3 h-32"},
            React.createElement("div", { className: "" },
                React.createElement("div", { className: "flex items-center" },
                    React.createElement("div", { className: "ml-0" },
                        React.createElement("div", { className: "flex items-center" },
                            React.createElement("div", { className: "mr-2 font-bold text-white" }, name),
                        ),
                    )
                ),
                React.createElement("div", { className: "text-sm  mt-2" },`${tasksCompleted} from ${classCompleted} attended`),
                React.createElement("svg", { className: "w-44 mt-3", height: "6", viewBox: "0 0 200 6", fill: "none", xmlns: "http://www.w3.org/2000/svg"},
                    React.createElement("rect", { width: "200", height: "6", rx: "3", fill: "#2D2D2D"}),
                    React.createElement(animated.rect, { width: barPlayhead.to((i) => i * (tasksCompleted / classCompleted) * 200), height: "6", rx: "3", fill: "url(#paint0_linear)"}),
                    React.createElement("rect", { x: "38", width: "2", height: "6", fill: "#171717"}),
                    React.createElement("rect", { x: "78", width: "2", height: "6", fill: "#171717"}),
                    React.createElement("rect", { x: "118", width: "2", height: "6", fill: "#171717"}),
                    React.createElement("rect", { x: "158", width: "2", height: "6", fill: "#171717"}),
                    React.createElement("defs",null,
                        React.createElement("linearGradient",{ id: "paint0_linear", x1: "0", y1: "0", x2: "1", y2: "0"},
                            React.createElement("stop", { stopColor: "#8E76EF" }),
                            React.createElement("stop", { offset: "1", stopColor: "#3912D2" })
                        )
                    )
                )
            ),
            <div className = "flex flex-col-2 items-center" >
                <div className = { "font-bold text-lg " + ( rise ? "text-green-500" : "text-red-500" )}>
                    {transactionAmount}%
                </div>
            </div>
                
            )
        )
    );
}


function Home() {

    const token = sessionStorage.getItem("token");
    
    return(
        <div>
            {token && token!== "" && token!==undefined ? <div>
                <h1 className='mt-12 ml-12 content-end font-bold text-white text-2xl'>Attendance Tracker</h1>
                <Content />
                <Logout />
            </div>:         
            <div><h1 className='mt-12 ml-12 content-end font-bold text-white text-2xl'>Unauthorized!</h1></div>}
        </div>
    )
        

        
    }


export default Home;