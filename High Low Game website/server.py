import random
from flask import Flask, request

app = Flask(__name__)

# Generate a random CPU number
cpu_number = random.randint(0, 9)
print(f"CPU number is: {cpu_number}")

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        return guess_number(user_guess)
    return ("""
        <h1 style='text-align: center'>Guess a number between 0 and 9</h1>
        <form method="POST" style='text-align: center'>
            <input type="number" name="guess" min="0" max="9" required>
            <input type="submit" value="Submit Guess">
        </form>
        <img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp' style='display: block; margin: auto;'>
    """)

def guess_number(number):
    if number == cpu_number:
        return ("""
            <h1 style='text-align: center; color: red'>That's the correct guess!</h1>
            <img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXl4eWUxYzZhcXF1bzl5dXAyM3dvZ3Nka3N3Zzk3Z3JlMmVlNHBlciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUOwGlX0dlYV3mQIzS/giphy.webp' style='display: block; margin: auto;'>
            <img src='https://i.pinimg.com/originals/d0/09/67/d009678eb5b1658468704f51bfc11173.gif' style='display: block; margin: auto;' width='520px'>
            <br><a href="/" style="text-align: center; color: red;">Play again</a>


        """)
    elif number < cpu_number:
        return ("""
            <h1 style='text-align: center'>That's too low!</h1>
            <img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGs5eGlvY3FmYmhrM2MxbzgydXZ6cHd1Zm9tOWtvcmMyMnZsa2FldCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jyEM1C2euOklQ18qrq/giphy.webp' style='display: block; margin: auto;'>
            <br><a href="/" style="text-align: center; color: red;">Try again</a>


        """)
    elif number > cpu_number:
        return ("""
            <h1 style='text-align: center'>That's too high!</h1>
            <img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3V0ZzRpaTVqbzc5Y3FyZDB0MTZjcDJoamUwZTZuZHZmN2Q4dGprMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1qOHsrZBFQqMmSwQBG/giphy.webp' style='display: block; margin: auto;'>
            <br><a href="/" style="text-align: center; color: red;">Try again</a>


        """)

if __name__ == "__main__":
    app.run(debug=True)
