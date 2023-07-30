install:
	#pip install build
	pip install ./

dev:
	pip install -e ./

test:
	pytest --junitxml=junit/test-results.xml --cov=settus --cov-report=xml --cov-report=html tests

coverage:
	open htmlcov/index.html

build:
	#pip install build
	python -m build

publish:
	python -m build
	twine upload dist/*