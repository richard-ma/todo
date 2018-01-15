import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

function TaskBadge(props) {
  if (props.status) {
    return (<span className="badge badge-warning">Done</span>);
  } else {
    return (<span className="badge badge-success">Processing</span>);
  }
}

class Task extends Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);

    this.state = {
      id: this.props.id,
      name: this.props.name,
      status: this.props.status,
    };
  }

  handleClick(e) {
    // TODO Update API
    this.setState((prevState) => ({
      status: !prevState.status
    }));
  }

  render() {
    return (
      <li className="list-group-item" onClick={this.handleClick}>
        <TaskBadge status={this.state.status}/>
        <span className="form-check-label">{this.state.name}</span>
      </li>
    );
  }
}

class App extends Component {
  render() {
    return (
      <ul className="list-group">
        <Task name='hello' status={true} />
        <Task name='hi' status={false} />
      </ul>
    );
  }
}

export default App;
