NAME=dkms_e1000e_bootfix
VERSION=4.10.14.patch1
DKMS_DIR=/usr/src/$(NAME)-$(VERSION)/

default:
	echo "See Makefile for possible targets"

install:
	install -m 755 -d $(DKMS_DIR)
	install -m 644 dkms.conf $(DKMS_DIR)/
	install -m 755 -d $(DKMS_DIR)/src/e1000e
	install -m 644 -t $(DKMS_DIR)/src/e1000e src/e1000e/*
	install -m 755 -d $(DKMS_DIR)/patches
	install -m 644 -t $(DKMS_DIR)/patches patches/*

rpm:
	rpmdev-setuptree
	tar --transform "s/^/$(NAME)-$(VERSION)\//" -zcvf ~/rpmbuild/SOURCES/$(NAME)-$(VERSION).tgz dkms.conf src/ patches/
	cp $(NAME).spec ~/rpmbuild/SPECS/
	rpmbuild -ba ~/rpmbuild/SPECS/$(NAME).spec
