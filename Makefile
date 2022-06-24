setup:
	#python3 -m venv ~/.myrepo
    python3 -m venv venv

install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=myrepolib tests/*.py
	python -m pytest --nbval notebook.ipynb


lint:
	#pylint --disable=R,C myrepolib cli web
	pylint --disable=R,C app_cap

all: install lint test