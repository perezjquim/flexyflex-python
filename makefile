main: update repackage

update:
	@echo "@Updating files...@"
	@cp -R flexyflex-python/* flexyflex-deb/opt/flexyflex-python/
	@echo "@Files updated!@"

repackage:
	@echo "@Repackaging...@"
	@dpkg-deb --build flexyflex-deb flexyflex-install.deb > /dev/null
	@echo "@Repackaged!@"
