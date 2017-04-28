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
	docker build -t summary_per_day --no-cache --rm . | tee build.log || exit 1

do-docker-tag:
	docker tag summary_per_day mlhamel/summary_per_day || exit 1

do-docker-push:
	docker push mlhamel/summary_per_day
