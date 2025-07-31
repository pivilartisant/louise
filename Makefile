get-data:
	python3 data/scripts/data.py
get-images:
	python3 data/scripts/get_images.py
lint-format:
	uv run ruff check --fix & uv run ruff format