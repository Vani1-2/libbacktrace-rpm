srpm:
	$(eval VERSION := $(shell grep "Version:" libbacktrace.spec | awk '{print $$2}'))
	git archive --format=tar.gz --prefix=libbacktrace-$(VERSION)/ -o libbacktrace-$(VERSION).tar.gz HEAD
	rpmbuild -bs --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)" libbacktrace.spec
