subarch: amd64
target: stage4
version_stamp: plasma-@latest@
rel_type: plasma
profile: default/linux/amd64/13.0/desktop/plasma/systemd
snapshot: @latest@
source_subpath: systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/releases/weekly/portage/sso

stage4/use:
	bindist
	ipv6

stage4/packages:
	kde-plasma/plasma-meta
	kde-apps/dolphin
	kde-apps/konsole

stage4/root_overlay: @REPO_DIR@/releases/weekly/overlays/plasma

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
