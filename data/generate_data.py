import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

n = 50000

cities = ["Bangalore", "Delhi", "Mumbai", "Hyderabad", "Chennai", "Pune"]
vehicle_types = ["Mini", "Prime", "Auto", "SUV"]
payment_methods = ["UPI", "Cash", "Card", "Wallet"]
ride_statuses = ["Completed", "Cancelled", "No Show"]

start_date = datetime(2024, 1, 1)

data = []

for i in range(1, n+1):
    date = start_date + timedelta(minutes=random.randint(0, 525600))
    city = random.choice(cities)
    vehicle = random.choice(vehicle_types)
    payment = random.choice(payment_methods)
    
    status = np.random.choice(
        ride_statuses,
        p=[0.78, 0.17, 0.05]
    )
    
    distance = round(np.random.uniform(2, 25), 2)
    
    base_fare = 40
    per_km = 12
    surge_multiplier = np.random.choice([1,1,1.2,1.5,2], p=[0.5,0.2,0.15,0.1,0.05])
    
    fare = 0
    if status == "Completed":
        fare = round((base_fare + distance * per_km) * surge_multiplier, 2)
    
    data.append([
        i, date, city,
        random.randint(1000, 2000),
        random.randint(5000, 20000),
        status, distance,
        fare, payment,
        vehicle, surge_multiplier
    ])

columns = [
    "ride_id","datetime","city","driver_id",
    "customer_id","ride_status","distance_km",
    "fare_amount","payment_method",
    "vehicle_type","surge_multiplier"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("ola_rides_50k.csv", index=False)

print("Dataset Generated Successfully!")