# .copr/Makefile
outdir ?= .

srpm:
	# 1. Install tools
	# dnf install -y git rpm-build

	# 2. Extract Version (Robustly: grab only the first match)
	$(eval VERSION := $(shell grep "^Version:" libbacktrace.spec | head -n 1 | awk '{print $$2}'))

	# DEBUG: Print what we found to the console
	@echo "DEBUG: Detected Version is '$(VERSION)'"

	# 3. Create tarball
	# If this fails, check the DEBUG line above!
	git archive --format=tar.gz --prefix=libbacktrace$(VERSION)/ -o libbacktrace$(VERSION).tar.gz HEAD

	# 4. Build SRPM
	rpmbuild -bs --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)" libbacktrace.spec
