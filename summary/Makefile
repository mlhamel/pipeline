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
	docker build -t summary --no-cache --rm --force-rm . | tee build.log

do-docker-tag:
	docker tag summary:latest mlhamel/summary:latest

do-docker-push:
	docker push mlhamel/summary
