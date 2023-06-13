from apscheduler.schedulers.blocking import BlockingScheduler
from pythonauto import send_me


sched = BlockingScheduler()

sched.add_job(send_me, 'interval', seconds=10)

sched.start()