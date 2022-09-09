
## SETUP

##### \# checkout
git clone git@github.com:dba-johnny/pokemon-crawler.git


##### \# basic venv setup [assuming scrapy linux dependencies are installed]
cd pokemon-crawler/ \
python3.8 -m venv .venv \
source .venv/bin/activate \
python -m pip install -r requirements.txt


##### \# django setup
cd pokemon/ \
python manage.py migrate \
python manage.py createsuperuser  	&emsp; \# enter username/password at prompt and remember for later 


##### \# run spider 
cd api\_crawler/ \
vim api\_crawler/settings.py \
&emsp; # find placeholder <REPO_PATH> and replace with local path to git repo \
scrapy crawl pspider --logfile pokemon-spider.log --loglevel INFO 


##### \# run admin screens to view crawled data 
cd pokemon/ \
python manage.py runserver		&emsp; \# goto localhost:8000/admin and login to view crawled data 


##### \# schedule hourly/daily crawls etc 
###### \# NB after first run, subsequent executions of pokemon spider will [i] update changes (if any) to all existing stored pokemons and [ii] find and store any newly defined pokemon 
cd api\_crawler/ \
python scrapy\_schedule.py --help	&emsp; \# follow instructions to schedule scrapy 


## NOTES
- Design & Implementation: I think these are reasonably self-explanatory, though there are some useful comments in the 'api\_crawler.api\_crawler.items' module
- Scalability: it is written with reasonable scalability in mind, but I would want to double check the \# db hits per page of crawled data (whilst I have of course taken relevant precautions etc, e.g. prefetch\_related for m2m queries, such things are worth being certain of when scaling up).
- Testing: to test end to end, probably worth building a test api with a known toy dataset which includes all relations defined in 'pokemon.pokemon\_app.models' module. Check data . This can test both data loads and data updates.
