import React, { Component } from 'react';
import {Grid, Button, ButtonGroup, Typography} from '@material-ui/core';
import {Link} from 'react-router-dom';
import RoomCreatePage from './RoomCreatePage';

export default class Room extends Component {
    constructor(props) {
        super(props);
        this.state = {
            votesToSkip: 2,
            guestCanPause: false,
            isHost: false,
            showSettings: false,
        };
        console.log(props);
        this.roomCode = this.props.match.params.roomCode;
        this.getRoomDetails();
        this.leaveButtonPressed = this.leaveButtonPressed.bind(this);
        this.updateShowSettings = this.updateShowSettings.bind(this);
        this.renderSettingsButton = this.renderSettingsButton.bind(this);
        this.renderSettings = this.renderSettings.bind(this);
    }

    getRoomDetails() {
        fetch('/polls/getroom' + '?code=' + this.roomCode)
            .then((response) => { 
                if (!response.ok) {
                    this.props.leaveRoomCallback();
                    this.props.history.push('/');
                }
                return response.json();
            })
            .then((data) => {
                this.setState({
                    votesToSkip: 100,
                    guestCanPause: false,
                    isHost: data.is_host,
                });
        });
    }

    leaveButtonPressed() {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
        };
        fetch('/polls/leaveroom', requestOptions)
            .then((_response) => {
                this.props.history.push('/');
        });
    }

    updateShowSettings(value) {
        this.setState({
            showSettings: value,
        })
    }

    renderSettingsButton() {
        return (
            <Grid item xs={12} align="center">
                <Button variant="contained" color="primary" onClick={() => this.updateShowSettings(true)}>
                    Settings
                </Button>
            </Grid>
        );
    }

    renderSettings() {
        return ( 
        <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <RoomCreatePage 
                    update={true} 
                    votesToSkip={this.state.votesToSkip} 
                    guestCanPause={this.state.guestCanPause}
                    roomCode={this.state.roomCode}
                    updateCallback={null}    
                />
            </Grid>
            <Grid item xs={12} align="center">
                <Button variant="contained" color="secondary" onClick={() => this.updateShowSettings(false)}>
                    Close
                </Button>
            </Grid>
        </Grid>
        );
    }

    render() {
        if (this.state.showSettings) {
            return this.renderSettings();
        }
        return <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography variant="h4" component="h4">
                    Code: {this.roomCode}
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Typography variant="h6" component="h6">
                    Votes to Skip: {this.state.votesToSkip}
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Typography variant="h6" component="h6">
                    Guest can Pause: {this.state.guestCanPause.toString()}
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Typography variant="h6" component="h6">
                    Host: {this.state.isHost.toString()}
                </Typography>
            </Grid>
            {this.state.isHost ? this.renderSettingsButton() : null}
            <Grid item xs={12} align="center">
                <Button variant="contained" color="secondary" onClick={this.leaveButtonPressed}>Leave room</Button>
            </Grid>
        </Grid>
    }
}

/*
<div>
    <h3>{this.roomCode}</h3>
    <p>Votes: {this.state.votesToSkip}</p>
    <p>Guest can pause: {this.state.guestCanPause.toString()}</p>
    <p>Host: {this.state.isHost.toString()}</p>
</div>
*/