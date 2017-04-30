.SHELLFLAGS = -e
.PHONY: docker-build
.NOTPARALLEL:

default: build

build: docker-build
docker-build: do-docker-build

tag: docker-tag
docker-tag: do-docker-tag

push: docker-push
docker-push: do-docker-push

test:
	python -m unittest discover .

do-docker-build:
	docker build -t fixed_time_sorting --no-cache --rm . | tee build.log

do-docker-tag:
	docker tag fixed_time_sorting mlhamel/fixed_time_sorting:latest

do-docker-push:
	docker push mlhamel/fixed_time_sorting
