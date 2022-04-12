import React from 'react';
import axios from 'axios';

export default class Test extends React.Component {
  state = {
    testData : "Rp"
  }

  componentDidMount() {
    axios.get(`http://localhost:5000/test`)
      .then(res => {
        console.log(res);
        const testData = res.data;
        this.setState({ testData });
      })
  }

  render() {
    return (
      <ul>
        {
          this.state.testData.message
        }
      </ul>
    )
  }
}