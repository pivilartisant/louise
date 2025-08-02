get-visualisation:
	PYTHONPATH=. python3 data/scripts/visualisation.py
get-general:
	 PYTHONPATH=. python3 data/scripts/general.py 
get-classification-examples:
	PYTHONPATH=. python3 -m data.scripts.images.get_image_for_classification
lint-format:
	uv run ruff check --fix & uv run ruff format