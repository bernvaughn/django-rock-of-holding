import React, { Component } from 'react';

export default class Room extends Component {
    constructor(props) {
        super(props);
        this.state = {
            votesToSkip: 2,
            guestCanPause: false,
            isHost: false,
        };
        console.log(props);
        this.roomCode = this.props.match.params.roomCode;
    }

    getRoomDetails() {
        fetch('/polls/getroom' + '?code=' + this.roomCode)
            .then((response) => response.json())
            .then((data) => {
                this.setState({
                    votesToSkip: 100,
                    guestCanPause: false,
                    isHost: data.is_host,
                })
            })
    }

    render() {
        return <div>
            <h3>{this.roomCode}</h3>
            <p>Votes: {this.state.votesToSkip}</p>
            <p>Guest can pause: {this.state.guestCanPause.toString()}</p>
            <p>Host: {this.state.isHost.toString()}</p>
        </div>
    }
}
