install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games