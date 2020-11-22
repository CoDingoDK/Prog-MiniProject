# PCSS Miniproject

**Run main.py to launch the game windows.**

As a proof of concept, running main.py will launch two windows without any object reference attachment to one another.
You are playing as two clients, and will select esports players for both teams, which will then battle eachother.

The core architecture of the networking is simple yet effective. Whenever a client interacts with the UI, the 
attached client passes an "action" ID (ints defined as constants for readability) to the server, occasionally along with
the data with which to perform said action. This allows for very adaptable execution of code across clients, as 
you can easily configure how a server should respond to any given action, and how the client should respond to a reply.
 
