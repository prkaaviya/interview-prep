"""job_scheduler.py"""


class Job:
    def __init__(self, name, job_time):
        self.name = name
        self.job_time = job_time

class Scheduler:
    def __init():
        


job1 = Job("job1", "9:00AM")
job2 = Job("job2", "10:15PM")

scheduler = Scheduler()

scheduler.schedule(job1)
scheduler.schedule(job2)

scheduler.run()