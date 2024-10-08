import random

# List of car brands
car_brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", 
              "BMW", "Mercedes", "Volkswagen", "Hyundai", "Kia"]

# Generate an array of car brands and random numbers
array_length = 10
random_car_array = [(random.choice(car_brands), random.randint(1, 10)) for _ in range(array_length)]

# Print the generated array
print("Array of car brands and random numbers:")
for index, (brand, number) in enumerate(random_car_array):
    print(f"Index {index}: {brand} - {number}")
print(random_car_array[0])
