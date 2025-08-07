from flask import Flask

app = Flask(__name__)

def convert_f_to_c(f):
    return (f - 32) * 5 / 9

@app.route("/f/<f_value>")
def fahrenheit(f_value):
    try:
        f_value = float(f_value)
        celsius = convert_f_to_c(f_value)
        return f"{f_value}°F = {round(celsius, 2)}°C"
    except ValueError:
        return "Invalid input! Please enter a number."

@app.route("/c/<f_value>")
def celsius(f_value):
    try:
        f_value = float(f_value)
        fahrenheit = (f_value * 9 / 5) + 32
        return f"{f_value}°C = {round(fahrenheit, 2)}°F"
    except ValueError:
        return "Invalid input! Please enter a number."


if __name__ == "__main__":
    app.run(debug=True)
