from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from whatsappauto import send_message

sched = BlockingScheduler()

sched.add_job(send_message, 'interval', seconds=10)

sched.start()