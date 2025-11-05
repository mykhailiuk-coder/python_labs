import numpy as np
import csv

def create_client():
    cities = ['Kyiv', 'Lviv', 'Odesa', 'Kharkiv']
    return {
        "age": np.random.randint(18, 70),
        "city": np.random.choice(cities),
        "total_spent": np.random.randint(500, 2000)
    }

clients = [create_client() for _ in range(10)]

try:
    with open('variant_17.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Age", "City", "Total Spent"])  

        for index, client in enumerate(clients, start=1):
            writer.writerow([client['age'], client['city'], client['total_spent']])
            print(f"Client {index}: Age={client['age']}, City={client['city']}, Total Spent={client['total_spent']}")
except FileNotFoundError:
    print("File was not found")
