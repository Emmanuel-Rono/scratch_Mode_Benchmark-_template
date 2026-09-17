.PHONY: setup test validate-demo
setup:
	python -m pip install -e .

test:
	python scripts/self_test.py

validate-demo:
	python scripts/validate_task.py task_template
	python scripts/validate_task.py example
