height = input("enter your height in m: ") #1.8 m
weight = input("enter your weight in kg: ") # 63 kg

# BMI = weight/ height^2

new_height = float(height)
new_weight = float(weight)
print(round(new_weight/(new_height * new_height)))