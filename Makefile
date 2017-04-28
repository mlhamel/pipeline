SUBDIRS := $(fixed_time_sorting summary_per_day)

.SHELLFLAGS = -e
.PHONY: test build $(SUBDIRS)
.NOTPARALLEL:

default: build

test:
	$(MAKE) -C fixed_time_sorting test
	$(MAKE) -C summary_per_day test
build:
	$(MAKE) -C fixed_time_sorting build
	$(MAKE) -C summary_per_day build
tag:
	$(MAKE) -C fixed_time_sorting tag
	$(MAKE) -C summary_per_day tag
push:
	$(MAKE) -C fixed_time_sorting push
	$(MAKE) -C summary_per_day push

create-pipeline:
	pachctl create-pipeline -f pipeline.json --push-images
update-pipeline:
	pachctl update-pipeline -f pipeline.json --push-images
