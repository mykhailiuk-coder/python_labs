import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv"]
clients = []

def get_client():
    new_client = {
        "age": int(np.random.randint(18, 70)),
        "city": str(np.random.choice(cities)),
        "total_spent": int(np.random.randint(300, 2000))
    }
    return new_client

def create_clients(n=500):
    clients.clear()
    for _ in range(n):
        client = get_client()
        clients.append(client)
    with open("variant_17.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["age", "city", "total_spent"])
        for client in clients:
            writer.writerow([client["age"], client["city"], client["total_spent"]])
    print(f"{n} clients written to variant_17.csv")
    return clients

def get_client_stats():
    df = pd.read_csv("variant_17.csv", sep=";")
    df["age_group"] = pd.cut(
        df["age"],
        bins=[18, 25, 35, 50, 70],
        labels=["18-25", "26-35", "36-50", "51-70"]
    )
    avg_spent_by_age_group = df.groupby("age_group", observed=True)["total_spent"].mean()
    print("\nСередні витрати по вікових групах:")
    print(avg_spent_by_age_group)

    total_spent_by_city = df.groupby("city")["total_spent"].sum()
    print("\nЗагальні витрати по містах:")
    print(total_spent_by_city)

    return avg_spent_by_age_group, total_spent_by_city

def get_plot_stats(avg_spent_by_age_group, total_spent_by_city):
    plt.figure(figsize=(8, 5))
    avg_spent_by_age_group.plot(kind='bar', color='skyblue')
    plt.title("Середні витрати по вікових групах")
    plt.xlabel("Вікова група")
    plt.ylabel("Середні витрати")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    plt.figure(figsize=(6, 6))
    total_spent_by_city.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title("Загальні витрати по містах")
    plt.ylabel("")
    plt.show()

create_clients(n=500)
avg_spent_by_age_group, total_spent_by_city = get_client_stats()
get_plot_stats(avg_spent_by_age_group, total_spent_by_city)
