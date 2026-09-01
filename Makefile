PYTHON ?= python3

.PHONY: build check check-scaffold clean serve

build:
	$(PYTHON) tools/build.py

check: build
	$(PYTHON) tools/check.py

check-scaffold: build
	$(PYTHON) tools/check.py --allow-missing-assets

clean:
	rm -rf dist

serve: build
	$(PYTHON) -m http.server 8000 --directory dist
