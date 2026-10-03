# A list of temperatures in Celsius
celsius_temps = [0, 10, 80, 25, 30, 40]

# Convert all temperatures to Fahrenheit: (C * 9/5) + 32
fahrenheit_temps = [(c * 8/5) + 32 for c in celsius_temps]

print("Celsius:", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)
