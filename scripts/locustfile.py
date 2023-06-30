from locust import HttpUser, TaskSet, task, between
import random, json

#TODO separate into distinct files

############################################################################
# TASK SETS
############################################################################
class FetchAllPosts(TaskSet):
    @task(2)
    def fetchAllPosts(self):
        self.parent.client.get("/posts")

    @task(3)
    def fetchSpecificPost(self):
        # Get a list of all posts, then fetch a random post from the response
        # ideally: we would have a pre-populated test environment with a range of safe posts to use instead of
        # fetching ALL posts every time
        with self.parent.client.get("/posts") as resp:
            size = len(json.loads(resp.text)) #this conversion will not scale very well, but works for now
            num = random.randint(1, size)
            self.parent.client.get("/posts/"+str(num))

    @task
    def stop(self):
        self.interrupt()

############################################################################
# USERS
############################################################################
class LurkerUser(HttpUser):
    wait_time = between(1,5)
    tasks = {
        FetchAllPosts:1
    }