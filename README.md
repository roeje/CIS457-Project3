#CIS 457 Project 3

##Python implementation of the classic Connect Four table top game

###Overview:
Net Four is a PTP multiplayer implementation of the classic board game Connect Four. The application consists of a centralized game server that keeps track of active players and allows users to query. Users are able to either host or search for a game while the central server stores their username and ip address. Other users can then look for games and pick one to join from a list provided in the console. Once connected to each other both players face off against each other using the animated user interface. The game and backend code is all written in python. The game is written using pygame, a game library for python. We used the built in socket library to handle all the network code

###Design:
Net Four operates using peer to peer networking. Each player launches a peer client or server and TCP sockets are utilize to send game moves between users. A matchmaking server that allows players to locate other users who have hosted a game and are waiting for an opponent. TCP socks are used to send a list of players from the matchmaking server to users who are searching for an opponent. The matchmaking server is always available and tracks users currently waiting for an opponent. 

When a user hosts a game, they are prompted to enter a username and then their game GUI is launched. Users searching for a game are presented with a list of all active hosts and they can select one to connect to. Once the connection is established between the two peers, the GUI for the connecting player is displayed and the game can start. 

As each player selects a move, data is sent over the connection between the peers to automatically update the state of the game board for both players. If a player wins, both are notified of the winner and the GUI clients can be closed, returning the players to the matchmaking client screen.

A custom logic engine was implemented to maintain the board state, check for win conditions and validate player moves. Unit tests were created to verify the accuracy of the logic functions.

The game board GUI was implemented using the pygame animation library. All player moves are animated for both players.

###Features:
* Multithreaded matchmaking server
* Thread safe data objects
* P2P connection between players
* Custom game logic library
* Custom space robot themed GUI implemented using the pygame animation library
* MVC design
* Unit testing for game logic classes
