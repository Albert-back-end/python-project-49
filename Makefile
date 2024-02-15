install:
	poetry install

lint:
	poetry run flake8 hexlet_python_package

build:  
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: build 