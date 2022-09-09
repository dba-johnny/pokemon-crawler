
## SETUP

\# checkout
git clone git@github.com:dba-johnny/pokemon-crawler.git


\# basic venv setup [assuming scrapy linux dependencies are installed]
cd pokemon-crawler/
python3.8 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt


\# django setup
cd pokemon/
python manage.py migrate
python manage.py createsuperuser  	\# enter username/password at prompt and remember for later


\# run spider
cd api\_crawler/
vim api\_crawler/settings.py
	# find placeholder <REPO_PATH> and replace with local path to git repo
scrapy crawl pspider --logfile pokemon-spider.log --loglevel INFO


\# run admin screens to view data
cd pokemon/
python manage.py runserver		\# goto localhost:8000/admin and login to view crawled data


\# schedule hourly/daily crawls etc
cd api\_crawler/
python scrapy\_schedule.py --help	\# follow instructions to schedule scrapy 


## TESTING
