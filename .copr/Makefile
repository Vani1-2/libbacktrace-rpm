PACKAGE_NAME = libbacktrace
VERSION = 1.0
SPEC_FILE = $(PACKAGE_NAME).spec


dist:
	git archive --format=tar.gz --prefix=$(PACKAGE_NAME)-master/ -o $(PACKAGE_NAME)-master.zip HEAD

srpm: dist
	rpmbuild \
		--define "_topdir $(PWD)/rpmbuild" \
		--define "_sourcedir $(PWD)" \
		--define "_specdir $(PWD)" \
		--define "_srcrpmdir $(PWD)" \
		-bs $(SPEC_FILE)
	@echo "SRPM generated at: $(PWD)/$(PACKAGE_NAME)-$(VERSION)-1.*.src.rpm"


clean:
	rm -rf rpmbuild $(PACKAGE_NAME)-master.zip *.src.rpm

.PHONY: dist srpm clean
