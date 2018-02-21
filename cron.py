from crontab import CronTab

my_cron = CronTab(user='mahad')
job = my_cron.new(command='python ~/Downloads/PycharmProjects/untitled9/writeDate.py')
job.minute.every(1)

my_cron.write()