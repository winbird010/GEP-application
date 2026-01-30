#!/user/bin/env python3
# -*- coding: utf-8 -*-

from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:8000"

    @task(5)
    def view_content(self):
        for slug in ["financing", "compensation", "trading", "damage", "others"]:
            self.client.get(f"/api/contents/{slug}")

    @task(1)
    def health(self):
        self.client.get("/api/health")
