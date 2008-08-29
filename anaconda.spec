# TODO
# - code poldek backend (python-poldek pkg exists!)
# - pldize /etc/fstab
# - /etc/modprobe.conf for geninitrd
#
%define		rel	200808292136
Summary:	Graphical system installer
Summary(pl.UTF-8):	Graficzny instalator systemu
Name:		anaconda
Version:	11.4.1.%{rel}
Release:	1
License:	GPL
Group:		Applications/System
# http://team.pld-linux.org/~patrys/anaconda.git - origin/pld-branch
Source0:	%{name}-%{rel}.tar.bz2
# Source0-md5:	1a3e6c15b9080fef45b53c2a471383ce
URL:		http://fedoraproject.org/wiki/Anaconda
BuildRequires:	device-mapper-static >= 1.01.05
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	glib2-static
BuildRequires:	glibc-static
BuildRequires:	gtk+2-devel
BuildRequires:	isomd5sum-devel
BuildRequires:	libdhcp-devel
BuildRequires:	libdhcp-static
BuildRequires:	libdhcp4client-devel
BuildRequires:	libdhcp6client-devel
BuildRequires:	libnl-devel
BuildRequires:	libselinux-devel >= 1.6
BuildRequires:	libsepol-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	python-kickstart >= 1.42
BuildRequires:	python-rhpl
BuildRequires:	python-rpm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	sed >= 4.0
BuildRequires:	slang-static
BuildRequires:	zlib-static
Requires:	/etc/pld-release
Requires:	bdevid
Requires:	device-mapper >= 1.01.05
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	grubby
Requires:	hal
Requires:	hfsutils
Requires:	jfsutils
Requires:	lvm2
Requires:	mdadm
Requires:	python-bdevid >= 6.0.24
Requires:	python-booty >= 0.93
Requires:	python-cracklib
Requires:	python-dbus
Requires:	python-devel-tools
Requires:	python-iniparse
Requires:	python-kickstart >= 1.42
Requires:	python-libuser
Requires:	python-libxml2
Requires:	python-parted >= 1.8.9
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
Requires:	yum >= 2.5.1-3
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
Requires:	yum >= 2.4.0

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
# locale check
if [ "$(locale -a | grep -c en_US.utf8)" = 0 ]; then
	: "en_US.utf8 locale not available. build will fail!"
	: "Install glibc-localedb-all or compile it!"
	exit 1
fi

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

# for ./isys/lang.c:isysLoadKeymap()
%ifarch %{ix86}
cp -a loader2/keymaps-i386 $RPM_BUILD_ROOT%{_sysconfdir}/keymaps.gz
%endif
%ifarch ppc
cp -a loader2/keymaps-ppc $RPM_BUILD_ROOT%{_sysconfdir}/keymaps.gz
%endif
%ifarch %{x8664}
cp -a loader2/keymaps-x86_64 $RPM_BUILD_ROOT%{_sysconfdir}/keymaps.gz
%endif

%find_lang %{name}

%{!?debug:%py_postclean %{_libdir}/anaconda}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%{_sysconfdir}/keymaps.gz
/etc/security/console.apps/liveinst
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/liveinst
%attr(755,root,root) %{_bindir}/liveinst
%attr(755,root,root) %{_sbindir}/anaconda
%attr(755,root,root) %{_sbindir}/gptsync
%attr(755,root,root) %{_sbindir}/liveinst
%attr(755,root,root) %{_sbindir}/showpart
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
%{_libdir}/anaconda-runtime/boot/boot.msg
%{_libdir}/anaconda-runtime/boot/general.msg
%{_libdir}/anaconda-runtime/boot/grub.conf
%{_libdir}/anaconda-runtime/boot/options.msg
%{_libdir}/anaconda-runtime/boot/param.msg
%{_libdir}/anaconda-runtime/boot/rescue.msg
%{_libdir}/anaconda-runtime/boot/syslinux.cfg
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall.functions
%attr(755,root,root) %{_libdir}/anaconda-runtime/genmodinfo
%attr(755,root,root) %{_libdir}/anaconda-runtime/getkeymaps
%{_libdir}/anaconda-runtime/keymaps-override-*
%dir %{_libdir}/anaconda-runtime/loader
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/init
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/loader
%{_libdir}/anaconda-runtime/loader/loader.tr
%{_libdir}/anaconda-runtime/loader/unicode-linedraw-chars.txt
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
