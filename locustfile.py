import random
from locust import HttpUser, task, between

class ChurnModelUser(HttpUser):
    # Wait between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    @task(1)
    def check_health(self):
        """Hit the health endpoint"""
        self.client.get("/health")

    @task(3)
    def predict_churn(self):
        """Send a POST request to predict churn"""
        payload = {
            "CreditScore": random.randint(300, 850),
            "Geography": random.choice(["France", "Spain", "Germany"]),
            "Gender": random.choice(["Female", "Male"]),
            "Age": random.randint(18, 92),
            "Tenure": random.randint(0, 10),
            "Balance": round(random.uniform(0.0, 250000.0), 2),
            "NumOfProducts": random.randint(1, 4),
            "HasCrCard": random.choice([0.0, 1.0]),
            "IsActiveMember": random.choice([0.0, 1.0]),
            "EstimatedSalary": round(random.uniform(0.0, 200000.0), 2)
        }
        
        self.client.post("/predict", json=payload)
