# TODO
# - code poldek backend (python-poldek pkg exists!)
#
%define		rel	200903212129
Summary:	Graphical system installer
Summary(pl.UTF-8):	Graficzny instalator systemu
Name:		anaconda
Version:	11.5.0.23.%{rel}
Release:	3
License:	GPL
Group:		Applications/System
# http://team.pld-linux.org/~patrys/anaconda.git
Source0:	%{name}-%{rel}.tar.bz2
# Source0-md5:	fb56c92d2c83f5a356891b2b13c7fc7b
URL:		http://fedoraproject.org/wiki/Anaconda
BuildRequires:	NetworkManager-devel
BuildRequires:	audit-libs-devel
# will kill it in the future
BuildRequires:	curl
BuildRequires:	dbus-devel
BuildRequires:	device-mapper-devel >= 1.01.05
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	isomd5sum-devel
BuildRequires:	libdhcp-devel
BuildRequires:	libdhcp4client-devel
BuildRequires:	libdhcp6client-devel
BuildRequires:	libnl-devel
BuildRequires:	libselinux-devel >= 1.6
BuildRequires:	libsepol-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	python-kickstart >= 1.50
BuildRequires:	python-rhpl
BuildRequires:	python-rpm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel
BuildRequires:	zlib-devel
Requires:	/etc/pld-release
Requires:	NetworkManager
Requires:	bdevid
Requires:	cryptsetup-luks
Requires:	device-mapper >= 1.01.05
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	grubby
Requires:	hal
Requires:	hfsutils
Requires:	jfsutils
Requires:	lvm2
Requires:	mdadm
Requires:	pci-database
Requires:	python-bdevid >= 6.0.24
Requires:	python-booty >= 0.93-4
Requires:	python-cracklib
Requires:	python-dbus
Requires:	python-devel-tools
Requires:	python-iniparse
Requires:	python-kickstart >= 1.44
Requires:	python-libuser
Requires:	python-libxml2
Requires:	python-parted >= 2.0.8
Requires:	python-pyblock >= 0.32
Requires:	python-rhpl >= 0.216
Requires:	python-rpm >= 4.2-0.61
Requires:	python-selinux
Requires:	python-snack
Requires:	python-urlgrabber >= 2.9.8
Requires:	reiserfsprogs
Requires:	system-config-date >= 1.9.17
Requires:	tzdata
Requires:	util-linux
Requires:	xfsprogs
Requires:	yum >= 3.2.19
%ifnarch s390 s390x
Requires:	python-pyblock >= 0.7-1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl.UTF-8
Pakiet anaconda zawiera program, którego można użyć do zainstalowania
systemu. Pliki te mają niewiele zastosowań na już zainstalowanym
systemie.

%package gui
Summary:	Anaconda GTK+2 GUI
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	X11-OpenGL-core
Requires:	X11-Xserver
Requires:	X11-fonts
Requires:	python-gnome-canvas
Requires:	python-pygtk-glade
Requires:	system-config-date
Requires:	system-config-keyboard

%description gui
Anaconda GUI portion.

%package runtime
Summary:	Graphical system installer portions needed only for fresh installs
Summary(pl.UTF-8):	Elementy graficznego instalatora systemu potrzebne tylko przy nowych instalacjach
Group:		Applications/System
AutoReqProv:	false
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/strip
Requires:	X11
Requires:	createrepo >= 0.4.3
Requires:	gawk
Requires:	glibc >= 6:2.3.6-5.1
Requires:	kbd
Requires:	policycoreutils >= 1.30
Requires:	python
Requires:	python-libxml2
Requires:	python-rpm >= 4.2-0.61
Requires:	squashfs
Requires:	yum >= 3.2.19

%description runtime
The anaconda-runtime package contains parts of the installation system
which are needed for installing new systems. These files are used to
build media sets, but are not meant for use on already installed
systems.

%description runtime -l pl.UTF-8
Pakiet anaconda-runtime zawiera elementy instalatora potrzebne tylko
do instalowania nowych systemów. Pliki te służą do tworzenia zestawu
nośników, nie są przewidziane do używania na już zainstalowanych
systemach.

%package debug
Summary:	Sourcecode for Anaconda
Summary(pl.UTF-8):	Kod źródłowy Anacondy
Group:		Applications/System
AutoReqProv:	false
Requires:	%{name} = %{version}-%{release}

%description debug
Anaconda sourcecode for debugging purposes.

%description debug -l pl.UTF-8
Kod źródłowy Anacondy do celów diagnostycznych.

%prep
%setup -q -n %{name}-%{rel}

%build
%{__make} depend -j1 \
	PYTHON="%{__python}" \
	PYTHONINCLUDE="%{py_incdir}" \
	CC="%{__cc}"

%{__make} -j1 \
	PYTHON="%{__python}" \
	PYTHONINCLUDE="%{py_incdir}" \
	CC="%{__cc}" \
	REALCC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

./py-compile isys/isys.py

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install isys/isys.py[co] $RPM_BUILD_ROOT%{_libdir}/anaconda

%find_lang %{name}

%{!?debug:%py_postclean %{_libdir}/anaconda}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
#%{_sysconfdir}/keymaps.gz
/etc/security/console.apps/liveinst
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/liveinst
%attr(755,root,root) %{_sbindir}/anaconda
%attr(755,root,root) %{_sbindir}/liveinst
%ifnarch ppc
%attr(755,root,root) %{_sbindir}/gptsync
%attr(755,root,root) %{_sbindir}/showpart
%endif
%dir %{_libdir}/anaconda
%{_libdir}/anaconda/*.py[co]
%dir %{_libdir}/anaconda/installclasses
%{_libdir}/anaconda/installclasses/*.py[co]
%dir %{_libdir}/anaconda/textw
%{_libdir}/anaconda/textw/*.py[co]
%{_libdir}/anaconda/lang-names
%{_libdir}/anaconda/lang-table
%attr(755,root,root) %{_libdir}/anaconda/_isys.so

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mini-wm
%attr(755,root,root) %{_libdir}/anaconda/xutils.so
%{_desktopdir}/liveinst.desktop
%dir %{_libdir}/anaconda/iw
%{_libdir}/anaconda/iw/*.py[co]
%{_datadir}/anaconda

%if %{!?debug:0}%{?debug:1}
%files debug
%defattr(644,root,root,755)
%{_libdir}/anaconda/*.py
%{_libdir}/anaconda/installclasses/*.py
%{_libdir}/anaconda/iw/*.py
%{_libdir}/anaconda/textw/*.py
%endif

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/anaconda/*-stub
%dir %{_libdir}/anaconda-runtime
%dir %{_libdir}/anaconda-runtime/boot
%ifnarch ppc
%{_libdir}/anaconda-runtime/boot/boot.msg
%{_libdir}/anaconda-runtime/boot/general.msg
%{_libdir}/anaconda-runtime/boot/grub.conf
%{_libdir}/anaconda-runtime/boot/options.msg
%{_libdir}/anaconda-runtime/boot/param.msg
%{_libdir}/anaconda-runtime/boot/rescue.msg
%{_libdir}/anaconda-runtime/boot/syslinux.cfg
%else
%{_libdir}/anaconda-runtime/boot/bootinfo.txt
%{_libdir}/anaconda-runtime/boot/magic
%{_libdir}/anaconda-runtime/boot/mapping
%{_libdir}/anaconda-runtime/boot/ofboot.b
%{_libdir}/anaconda-runtime/boot/yaboot.conf.3264
%{_libdir}/anaconda-runtime/boot/yaboot.conf.in
%endif
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall.functions
%attr(755,root,root) %{_libdir}/anaconda-runtime/genmodinfo
%attr(755,root,root) %{_libdir}/anaconda-runtime/getkeymaps
%attr(755,root,root) %{_libdir}/anaconda-runtime/makestamp.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/maketreeinfo.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/mapshdr
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.alpha
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.ia64
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.efi
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.ppc
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.s390
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.x86
%attr(755,root,root) %{_libdir}/anaconda-runtime/modlist
%attr(755,root,root) %{_libdir}/anaconda-runtime/pyrc.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/readmap
%attr(755,root,root) %{_libdir}/anaconda-runtime/scrubtree
%{_libdir}/anaconda-runtime/screenfont-*.gz
%attr(755,root,root) %{_libdir}/anaconda-runtime/trimpciids
%attr(755,root,root) %{_libdir}/anaconda-runtime/upd-instroot
%attr(755,root,root) %{_libdir}/anaconda-runtime/upd-updates
