# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

# getting data from user
weight = float(input('Please enter your weight (kg)'))
height = float(input('Please enter your height (m)'))

# BMI formula
bmi = weight / (height ** 2)
# Rounding the result
bmi_rounded = round(bmi, 1)

# conditions
if bmi_rounded < 18.5 :
    print('Your BMI classification is:', bmi_rounded, '==> Underweight')
elif 18.5 < bmi_rounded <= 24.9 :
    print('Your BMI classification is:', bmi_rounded, '==> Normal weight')
elif 25.0 < bmi_rounded <= 29.9 :
    print('Your BMI classification is:', bmi_rounded, '==> Overweight')
elif 30.0 < bmi_rounded :
    print('Your BMI classification is:', bmi_rounded, '==> Obese')
