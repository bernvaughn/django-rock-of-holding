import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import Room from "./Room";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import RoomCreatePage from "./RoomCreatePage";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>This is the home page</p>
          </Route>
          <Route path="/join" component={RoomJoinPage} />
          <Route path="/create" component={RoomCreatePage} />
          <Route path="/room/:roomCode" component={Room} />
        </Switch>
      </Router>
    );
  }
}