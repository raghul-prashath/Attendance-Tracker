import React from 'react';
import axios from 'axios';

export default class Test extends React.Component {
  state = {
    testData : "Hello World!"
  }

  componentDidMount() {
    axios.get("/user/test")
      .then(res => {
        console.log(res);
        const testData = res.data;
        this.setState({ testData });
      })
  }

  render() {
    return (
      <ul>
        Hey !
        {
          this.state.testData.message
        }
      </ul>
    )
  }
}