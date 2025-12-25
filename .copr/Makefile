PACKAGE_NAME = libbacktrace
outdir ?= $(PWD)


srpm:
	
	dnf install -y git
	$(eval VERSION := $(shell grep "Version:" $(PACKAGE_NAME).spec | awk '{print $$2}'))
	git archive --format=tar.gz --prefix=$(PACKAGE_NAME)-$(VERSION)/ -o $(PACKAGE_NAME)-$(VERSION).tar.gz HEAD
	rpmbuild -bs --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)" $(PACKAGE_NAME).spec

clean:
	rm -f *.tar.gz *.src.rpm

.PHONY: srpm clean
