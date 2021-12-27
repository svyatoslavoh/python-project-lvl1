first-install:
	pip3 install poetry
	poetry config virtualenvs.create true
	poetry config virtualenvs.in-project true

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even 

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd 

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games