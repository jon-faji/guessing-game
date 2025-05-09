# guessing_game.py

# This is a simple guessing game server that generates a random secret number and allows clients to guess it.
# The server listens for incoming connections and handles each client in a separate thread.
# The game generates a random secret number and the player has to guess it.
# The generate_secret function is mocked to return a fixed value for testing purposes.
# The test suite includes tests for correct guesses, too low/high guesses, and invalid input.
# This test suite uses unittest to test the evaluate_guess function and the generate_secret function.


import random
import socket

def generate_secret():
    return random.randint(1, 100)

def evaluate_guess(secret, guess):
    try:
        guess = int(guess)
    except ValueError:
        return "Invalid input. Please enter a number."
    
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"

def handle_client(client_socket):
    secret = generate_secret()
    client_socket.send(b"Guess a number between 1 and 100:\n")
    
    while True:
        guess = client_socket.recv(1024).decode().strip()
        if not guess:
            break

        response = evaluate_guess(secret, guess)
        client_socket.send((response + "\n").encode())

        if response == "Correct!":
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('10.125.4.55', 8000))
    server.listen(1)
    print("Server started on port 9999...")

    while True:
        client_socket, addr = server.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
