"""
    calculate social security fee
"""
# enter the salary
salary = float(input("Enter the salary:"))

# calculate the social security fee
social_security_fee = salary * (0.08 + 0.02 + 0.002 + 0.12) + 3

# print the social security fee
print("Social security fee:" + str(social_security_fee))
