"""
3. Write a program which prompts the user to enter the mass in pounds,
converts the mass to kg, and prints:
a. The converted mass in kgs (1 kg = 2.20462 lbs)
b. The weight of the mass on Earth (Newtons)  = mass (kg) x 9.807 (m/s^2)
c. The weight of the mass on the Moon (Newtons)  = mass (kg) x 1.62 (m/s^2)
d. The percentage of the weight on the Moon in comparison to what is experienced
on Earth = Weight on Moon / Weight on Earth x 100
e. The percentage of the weight on the Moon in comparison to what is experienced
 on Earth as an integer"""


mass = input("Please enter the mass in lb that you would kile to convert to kg: ")

msTokg = (float(mass) / 2.20462)
print("The converted mass in kg is: ", msTokg)

earthmass = msTokg * 9.807
print("Your weight on Earth is: ", earthmass ,"Newtons")

moonmass = msTokg * 1.62
print("Your weight on the Moon is: " , moonmass , "Newtons")

weightPer1 = moonmass / earthmass * 100
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth:" , weightPer1 ,"%")

weightPer2 = int(round(moonmass / earthmass * 100))
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is" , weightPer2 , "%")
