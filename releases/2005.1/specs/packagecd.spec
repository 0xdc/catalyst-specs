subarch: alpha
version_stamp: 2005.1
target: grp
rel_type: default
profile: default-linux/alpha/2005.0
snapshot: 20050709
distcc_hosts: localhost/5 alpha10.crl.dec.com/5
source_subpath: default/stage3-alpha-2005.1
grp: src cd2

grp/use: 
	bonobo
	cdr
	dvd
	dvdr
	esd 
	gtkhtml 
	mozilla
	ruby
	tcltk
	ldap
	socks5
#	fbcon
#	atm

grp/src/type: srcset
grp/src/packages:
	dhcpcd
	slocate
	udev
	dcron
#	fcron
	vixie-cron
#	gentoo-sources
	vanilla-sources
	coldplug
#	fxload
	syslog-ng
	logrotate
	raidtools
	nfs-utils
#	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	rp-pppoe
#	penggy
	iputils
#	lvm2
#	evms
	pptpclient
	mdadm
	ethtool
#	wireless-tools
#	prism54-firmware
#	wpa_supplicant
	genkernel
#	lilo
#	grub
#	dante
	tsocks
#	splashutils
#	splash-themes-livecd
#	pcmcia-cs
#	slmodem
#	globespan-adsl
#	hostap-driver
#	hostap-utils
#	ipw2100
#	ipw2200
#	fritzcapi
#	fcdsl
#	acpid
#	cryptsetup
#	nvidia-kernel
#	nvidia-glx
#	ati-drivers
#	alsa-lib
#	alsa-oss
#	alsa-utils
#	alsa-driver

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
#	gentoo-sources
	irssi
	gpm
	parted
	links
	dosfstools
#	ntfsprogs
	screen
	mirrorselect
	vim
	xscreensaver
#	ide-smart
	netcat
#	gpart
	gnupg
	sys-apps/eject
	minicom
	whois
	tcpdump
	cvs
	zip
	unzip
#	partimage
	app-admin/sudo
	app-cdr/cdrtools
	gnome
	emacs
	dev-lang/ruby
	enlightenment
	kde
	mozilla-firefox
	mozilla-thunderbird
	xfce4
#	openbox
	fluxbox
	sylpheed
	xemacs
	xmms
	abiword
	gaim
	xchat
	tetex
#	k3b
	koffice
	samba
	nmap
	ettercap
	mplayer
