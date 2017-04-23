.SHELLFLAGS = -e
.PHONY: test
.NOTPARALLEL:

default: test
test:
	python -m unittest discover fixed_time_sorting
