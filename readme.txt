Number Guessing Game

1. What the program does
This program is a simple interactive terminal game where the computer selects a random number between 1 and 100, and the user must guess what it is. After each guess, the program provides feedback on whether the guess was "Too low" or "Too high". Once the user guesses the correct number, the game ends and displays the total number of attempts made.

2. How to run it
You need Python installed on your computer to run this game. 
Open your terminal or command prompt, navigate to the folder containing the file "NumberGuessingGame.py", and run the following command:
python main.py

If "python" does not work depending on your setup, you can try:
python3 NumberGuessingGame.py

3. Known limitations
- The lower and upper bounds of the guessing range (1 to 100) are hardcoded and cannot be changed without modifying the code.
- The game runs indefinitely until the correct number is guessed or the program is forcibly terminated. There is no option to quit midway.
- Playing again requires re-running the script.
