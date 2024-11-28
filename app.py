from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Fungsi untuk konversi dari Celcius ke Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fungsi untuk konversi dari Fahrenheit ke Celcius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk konversi suhu
@app.route('/convert', methods=['POST'])
def convert_temperature():
    # Mendapatkan data dari form
    scale = request.form.get('scale')
    value = request.form.get('value', type=float)

    if scale not in ['C', 'F'] or value is None:
        return render_template('index.html', error="Masukkan temperatur dengan benar.")

    if scale == 'C':
        result = celsius_to_fahrenheit(value)
        return render_template('index.html', input=f"{value}°C", output=f"{result:.2f}°F")
    elif scale == 'F':
        result = fahrenheit_to_celsius(value)
        return render_template('index.html', input=f"{value}°F", output=f"{result:.2f}°C")

if __name__ == '__main__':
    app.run(debug=True)
