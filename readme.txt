Number Guessing Game

1. What the program does
This program is a simple interactive terminal game where the computer selects a random number between 1 and 100, and the user must guess what it is. After each guess, the program provides feedback on whether the guess was "Too low" or "Too high". Once the user guesses the correct number, the game ends and displays the total number of attempts made.

2. How to run it
You need Python installed on your computer to run this game. 
Open your terminal or command prompt, navigate to the folder containing the file "main.py", and run the following command:
python main.py

If "python" does not work depending on your setup, you can try:
python3 main.py

3. Known limitations
- The lower and upper bounds of the guessing range (1 to 100) are hardcoded into the program and cannot be changed without modifying the source code.
- The game runs indefinitely until the correct number is guessed or the program is forcibly terminated (e.g., using Ctrl+C). There is no option to quit midway through the prompts gracefully.
- Re-playing the game requires re-running the script, as there is no prompt asking the user if they want to play again after a win.
