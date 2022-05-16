import subprocess
from subprocess import PIPE

subprocess.run('scrapy runspider editais.py -O edital.json', stderr=PIPE, stdout=PIPE)
