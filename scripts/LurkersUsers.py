from locust import HttpUser, between
from TaskSets import FetchAllPosts

class LurkerUser(HttpUser):
    weight = 243 #per load analysis
    wait_time = between(1, 5)
    tasks = {
        FetchAllPosts:1
    }