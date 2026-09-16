# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 3

import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
import os
import random

os.makedirs("charts", exist_ok=True)

fake = Faker()
QUESTION = "How many people are over the age of 40 in this dataset?"

def generate_dataset(n=5000):
    data = []
    for _ in range(n):
        person={
            "name": fake.name(),
            "age": random.randint(18, 80),
            "city": fake.city(),
            "income": random.randint(20000, 200000)
        }
        data.append(person)

    df = pd.DataFrame(data)
    df.to_csv("data/people.csv", index=False)
    print("Generated data/people.csv")


def analyze():
    df = pd.read_csv("data/people.csv")
    filtered=df[df["age"] > 40]
    count = len(filtered)
    print(f"People over the age of 40: {count}")
    return filtered

def get_age_ranges(filtered):
    ages = {
            "40-49": 0,
            "50-59": 0,
            "60-69": 0,
            "70-80": 0
        }

    for _, p in filtered.iterrows():
        age = p["age"]
        if(age < 50):
            ages["40-49"] += 1
        elif 50<=age<=59:
            ages["50-59"] += 1
        elif 60<=age<=69:
            ages["60-69"] += 1
        elif 70<=age<=80:
            ages["70-80"] += 1

    return ages

def visualize(df):
    plt.figure(figsize=(8,5))

    plt.bar(df.keys(), df.values(), color="skyblue")

    plt.ylim(0, max(df.values()))
    plt.yticks(range(0, (max(df.values()) + 1), 100))

    plt.title("Number of people over the age of 40")
    plt.xlabel("Age")
    plt.ylabel("People")

    output_path = "charts/people_over_40.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to {output_path}")

def main():
    os.makedirs("data",exist_ok=True)
    generate_dataset()
    filtered = analyze()
    ages = get_age_ranges(filtered)
    visualize(ages)

if __name__ == "__main__":
    main()