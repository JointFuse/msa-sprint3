from locust import HttpUser, task, constant

class RateLimitTester(HttpUser):
    wait_time = constant(0.001)

    @task
    def test_rate_limit(self):
        self.client.get("/api", headers={"Client-Type": "mobile"})
        self.client.get("/api", headers={"Client-Type": "web"})
