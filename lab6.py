import csv
import numpy as np
import pandas as pd

cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv"]

def get_client():
    new_client = {
        "age": int(np.random.randint(18, 70)),
        "city": str(np.random.choice(cities)),
        "total_spent": int(np.random.randint(300, 2000))
    }
    return new_client

clients = []

for i in range(500):
    client = get_client()
    clients.append(client)

with open("variant_17.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["age", "city", "total_spent"])
    for client in clients:
        writer.writerow([client["age"], client["city"], client["total_spent"]])

print("Written client data")
