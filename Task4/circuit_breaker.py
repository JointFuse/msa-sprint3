from locust import HttpUser, task, constant

class CircuitBreakerUser(HttpUser):
    wait_time = constant(0.001)

    @task
    def test_api(self):
        self.client.get("/logistics")
