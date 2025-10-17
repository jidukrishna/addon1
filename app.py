from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            height_m = height / 100
            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

            bmi = round(bmi, 2)
        except:
            category = "Invalid input. Please enter valid numbers."
            color = "gray"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
