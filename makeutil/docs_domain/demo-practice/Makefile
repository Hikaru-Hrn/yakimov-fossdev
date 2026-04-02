create-structure:
	mkdir -p src tests docs
	touch README.md setup.py requrements.txt
	touch docs/DOMAIN.md docs/SPECIFICATION.md
	touch src/.gitkeep tests/.gitkeep

install_deb:
	pip install -r requrements.txt

install:
	pip install -e

test_pytest:
	python3 -m pytest.py

venv:
	python3 -m venv .venv

setup:
	create_practice install_deb install
