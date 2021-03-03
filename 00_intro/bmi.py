weight = int(input('Please enter your weight (kg)'))
height = int(input('Please enter your height (cm)'))
BMI = (weight / (height ** 2))
BMI_rounded = (BMI, 2)

print('Your BMI rate is', BMI_rounded)
