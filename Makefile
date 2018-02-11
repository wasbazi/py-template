install:
	virtualenv -p $$(which python3) ./venv
	source ./venv/bin/activate && pip install -r requirements.txt
	echo "$$(tput 6)$$(tput bold)Don't forget to source venv/bin/activate$$(tput sgr0)"

requirements.txt: setup.py
	rm -rf venv || echo 'no previous venv'
	virtualenv -p $$(which python3) venv
	source ./venv/bin/activate && python setup.py install && pip freeze > requirements.txt
	rm -rf venv || echo 'no previous venv'

server-dev:
	python py-template/main.py
