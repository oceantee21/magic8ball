Magic 8 Ball (Python)
A simple Python Magic 8-Ball CLI that returns randomized answers to yes/no questions.

Features
Twenty classic Magic 8-Ball responses (affirmative, non-committal, negative).
Interactive command-line loop with input validation.
Easy to extend with custom responses.
Requirements
Python 3.8+
Installation
(Optional) Create and activate a virtual environment:
bash

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
(Optional) Upgrade pip:
bash

pip install --upgrade pip
Usage
bash

python magic8ball.py
Type a yes/no question and press Enter.
Read the answer.
Type y to ask again or any other key to quit.
Example RESPONSES
python

RESPONSES = [
  "It is certain.", "Without a doubt.", "You may rely on it.",
  "Yes — definitely.", "As I see it, yes.", "Most likely.",
  "Outlook good.", "Yes.", "Signs point to yes.",
  "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
  "Cannot predict now.", "Concentrate and ask again.",
  "Don't count on it.", "My reply is no.", "My sources say no.",
  "Outlook not so good.", "Very doubtful.", "No."
]
Suggested script structure
import random
define RESPONSES constant
run an input loop: prompt for question → validate non-empty → print random.choice(RESPONSES) → ask whether to continue
License
MIT

Author
oceantee21
killer999331@gmail.com