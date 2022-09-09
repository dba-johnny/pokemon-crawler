import schedule
import time
import os
import sys

from argparse import ArgumentParser
from datetime import datetime

def initiate_crawl():
    log_file = datetime.now().strftime('schedule-logs/pokemon-spider-%Y-%m-%d-%H:%M:%S.log')
    str_command = "scrapy crawl pspider --loglevel INFO --logfile %s" % log_file
    print("Executing Pokemon Spider....")
    print("\t\t %s" % str_command)
    os.system(str_command)
    print("Complete")


parser = ArgumentParser(description='Schedule Pokemon Spider')
parser.add_argument('--minutes', metavar='minutes', type=int, help='number of minutes between Pokemon Spider execution')
options = parser.parse_args()

if options.minutes:
    print('Scheduler initialised')
    schedule.every(options.minutes).minutes.do(initiate_crawl)
    print('First job is set to run at: ' + str(schedule.next_run()))
    print('Each subsequent job will run %s minute(s) after completion of previous' % str(options.minutes))

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    parser.print_help()
    print("", flush=True)
    sys.exit(0)
