SUBDIRS = fixed_time_sorting summary_per_day

.SHELLFLAGS = -e
.PHONY: test $(SUBDIRS)
.NOTPARALLEL:

default: update

test: $(SUBDIRS)
build: $(SUBDIRS)
tag: $(SUBDIRS)
push: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

create-pipeline:
	pachctl create-pipeline -f pipeline.json
update-pipeline:
	pachctl update-pipeline -f pipeline.json

update: build tag push update-pipeline
create:	build tag push create-pipeline
