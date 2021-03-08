weight = float(input('Please enter your weight (kg)'))
height = float(input('Please enter your height (m)'))

bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)

print('Your BMI rate is', bmi_rounded)
