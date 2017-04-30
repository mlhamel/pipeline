SUBDIRS = fixed_time_sorting summary

.SHELLFLAGS = -e
.PHONY: test $(SUBDIRS)
.NOTPARALLEL:

default: all

test: $(SUBDIRS)
build: $(SUBDIRS)
tag: $(SUBDIRS)
push: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

all: build tag push

create-pipeline:
	pachctl create-pipeline -f pipeline.json
update-pipeline:
	pachctl update-pipeline -f pipeline.json
