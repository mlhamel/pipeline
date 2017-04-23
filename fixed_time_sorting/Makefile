.SHELLFLAGS = -e
.PHONY: docker-build
.NOTPARALLEL:

default: build
build: docker-build
docker-build: do-docker-build

do-docker-build:
	docker build -t mlhamel/fixed_time_sorting --no-cache --rm . | tee build.log || exit 1
