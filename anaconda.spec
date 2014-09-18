# TODO
# - code poldek backend (python-poldek pkg exists!)
# - anaconda can't install packages: http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2013-May/023527.html
#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	live		# build livecd components

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).

# Also update in AM_GNU_GETTEXT_VERSION in configure.ac
%define gettextver 0.18.3
%define intltoolver 0.31.2-3
%define pykickstartver 1.99.58
%define yumver 3.4.3-9
%define dnfver 0.4.18
%define partedver 1.8.1
# git show 292c314
%define pypartedver 3.9
%define pythonpyblockver 0.45
%define nmver 0.9.9.0-10.git20130906
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.23-1
%define sckeyboardver 1.3.1
%define firewalldver 0.3.5-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 034-7
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
# git show 2b2418e
%define iscsiver 2.0.870-3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.18-1
%define libxklavierver 5.4
%define libtimezonemapver 0.4.1-2

%define md5	6f0d544a9b08287aa6d981208adc5bfa
Summary:	Graphical system installer
Summary(pl.UTF-8):	Graficzny instalator systemu
Name:		anaconda
Version:	22.4
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/anaconda/%{name}-%{version}.tar.bz2/%{md5}/anaconda-%{version}.tar.bz2
# Source0-md5:	6f0d544a9b08287aa6d981208adc5bfa
Patch0:		interfaces-dir.patch
Patch1:		libexec.patch
Patch2:		yum-comps.patch
Patch3:		product-defaults.patch
URL:		http://fedoraproject.org/wiki/Anaconda
BuildRequires:	NetworkManager-devel >= %{nmver}
BuildRequires:	audit-libs-devel
BuildRequires:	dbus-devel >= %{dbusver}
BuildRequires:	gettext >= %{gettextver}
BuildRequires:	glade-devel
#BuildRequires:	glib2-doc
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
#BuildRequires:	gtk3-devel-docs
BuildRequires:	intltool >= %{intltoolver}
BuildRequires:	libarchive-devel >= %{libarchivever}
#BuildRequires:	libgnomekbd-devel
#BuildRequires:	libtimezonemap-devel >= %{libtimezonemapver}
#BuildRequires:	libxklavier-devel >= %{libxklavierver}
BuildRequires:	pango-devel
BuildRequires:	python-dbus
BuildRequires:	python-devel
BuildRequires:	python-nose
BuildRequires:	python-pygobject3
#BuildRequires:	python-pykickstart >= %{pykickstartver}
BuildRequires:	python-urlgrabber >= %{pythonurlgrabberver}
BuildRequires:	rpm-devel >= %{rpmver}
#BuildRequires:	systemd
BuildRequires:	yum >= %{yumver}
%if %{with live}
BuildRequires:	desktop-file-utils
%endif
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	%{name}-tui = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl.UTF-8
Pakiet anaconda zawiera program, którego można użyć do zainstalowania
systemu. Pliki te mają niewiele zastosowań na już zainstalowanym
systemie.

%package core
Summary:	Core of the Anaconda installer
Requires:	NetworkManager >= %{nmver}
Requires:	authconfig
Requires:	chrony
Requires:	createrepo_c
Requires:	dhclient
Requires:	dnf >= %{dnfver}
Requires:	firewalld >= %{firewalldver}
Requires:	isomd5sum >= %{isomd5sum}
Requires:	kbd
Requires:	langtable-data >= %{langtablever}
Requires:	langtable-python >= %{langtablever}
Requires:	libreport-anaconda >= 2.0.21-1
Requires:	parted >= %{partedver}
Requires:	python-IPy
Requires:	python-blivet >= 0.61
Requires:	python-coverage
Requires:	python-dbus
Requires:	python-libuser
Requires:	python-meh >= %{mehver}
Requires:	python-nss
Requires:	python-ntplib
Requires:	python-parted >= %{pypartedver}
Requires:	python-pwquality
Requires:	python-pykickstart >= %{pykickstartver}
Requires:	python-pytz
Requires:	python-rpm >= %{rpmver}
Requires:	python-selinux
Requires:	python-selinux
Requires:	python-urlgrabber >= %{pythonurlgrabberver}
Requires:	realmd
Requires:	rsync
Requires:	systemd
Requires:	teamd
Requires:	util-linux >= %{utillinuxver}
Requires:	yum >= %{yumver}
Requires:	yum-utils >= %{yumutilsver}
# required because of the rescue mode and VNC question
Requires:	anaconda-tui = %{version}-%{release}
%if %{with live}
Requires:	desktop-file-utils
Requires:	usermode
%endif
%ifarch %{ix86} %{x8664}
Requires:	fcoe-utils >= %{fcoeutilsver}
%endif
Requires:	open-iscsi >= %{iscsiver}
%ifarch %{ix86} %{x8664} ia64
Requires:	dmidecode
Requires:	hfsplus-tools
%endif
Provides:	anaconda-images = %{version}-%{release}
Provides:	anaconda-runtime = %{version}-%{release}
Obsoletes:	anaconda-images <= 10
Obsoletes:	anaconda-runtime < %{version}-%{release}
Obsoletes:	booty <= 0.107-1

%description core
The anaconda-core package contains the program which was used to
install your system.

%package gui
Summary:	Graphical user interface for the Anaconda installer
Requires:	NetworkManager-wifi
Requires:	adwaita-icon-theme
Requires:	anaconda-core = %{version}-%{release}
Requires:	anaconda-widgets = %{version}-%{release}
Requires:	keybinder3
Requires:	libgnomekbd
Requires:	libtimezonemap >= %{libtimezonemapver}
Requires:	libxklavier >= %{libxklavierver}
Requires:	nm-connection-editor
Requires:	python-meh-gui >= %{mehver}
Requires:	system-logos
Requires:	tigervnc-server-minimal
Requires:	usermode
%if %{with live}
Requires:	zenity
%endif

%description gui
This package contains graphical user interface for the Anaconda
installer.

%package tui
Summary:	Textual user interface for the Anaconda installer
Group:		Applications/System
Requires:	anaconda-core = %{version}-%{release}

%description tui
This package contains textual user interface for the Anaconda
installer.

%package widgets
Summary:	A set of custom GTK+ widgets for use with anaconda
Group:		Libraries
Requires:	python
Requires:	python-pygobject3

%description widgets
This package contains a set of custom GTK+ widgets used by the
anaconda installer.

%package widgets-devel
Summary:	Development files for anaconda-widgets
Group:		Development/Libraries
Requires:	%{name}-widgets = %{version}-%{release}
Requires:	glade

%description widgets-devel
This package contains libraries and header files needed for writing
the anaconda installer. It also contains Python and Glade support
files, as well as documentation for working with this library.

%package dracut
Summary:	The anaconda dracut module
Group:		Applications/System
Requires:	dracut >= %{dracutver}
Requires:	dracut-network
Requires:	python-pykickstart
Requires:	xz

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the
anaconda runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# / on %{_prefix} kicks in
%{__sed} -i -e '1 s,#!/usr/bin/bash,#!/bin/sh,' scripts/run-anaconda

# TODO: driver_disk not compiling (needs rpm5 porting) disable.
%{__sed} -i -e '/SUBDIRS/ s/dd//' utils/Makefile.am

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-introspection \
	--enable-gtk-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	systemddir=%{systemdunitdir} \
	generatordir=%{systemdunitdir}-generators \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" | xargs %{__rm} -v

%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/tzmapdata

%if %{with live}
desktop-file-install ---dir=$RPM_BUILD_ROOT%{_desktopdir} $RPM_BUILD_ROOT%{_desktopdir}/liveinst.desktop
%endif

# unsupported locales
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bal
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ilo

%find_lang %{name}

%{!?debug:%py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with live}
%post
update-desktop-database

%postun
update-desktop-database
%endif

%post	widgets -p /sbin/ldconfig
%postun	widgets -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING

%files core -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING
%{systemdunitdir}/*
%{systemdunitdir}-generators/*
%attr(755,root,root) %{_bindir}/anaconda-cleanup
%attr(755,root,root) %{_bindir}/analog
%attr(755,root,root) %{_bindir}/instperf
%attr(755,root,root) %{_sbindir}/anaconda
%attr(755,root,root) %{_sbindir}/handle-sshpw

%{_datadir}/%{name}

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/anaconda-yum
%attr(755,root,root) %{_libdir}/%{name}/auditd
%attr(755,root,root) %{_libdir}/%{name}/run-anaconda
%attr(755,root,root) %{_libdir}/%{name}/upd-updates
%attr(755,root,root) %{_libdir}/%{name}/zram-stats
%attr(755,root,root) %{_libdir}/%{name}/zramswapoff
%attr(755,root,root) %{_libdir}/%{name}/zramswapon

%{py_sitedir}/pyanaconda
%exclude %{py_sitedir}/pyanaconda/rescue.py*
%exclude %{py_sitedir}/pyanaconda/text.py*
%exclude %{py_sitedir}/pyanaconda/ui/gui
%exclude %{py_sitedir}/pyanaconda/ui/tui

%if %{with live}
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/liveinst
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/liveinst
%attr(755,root,root) %{_bindir}/liveinst
%attr(755,root,root) %{_sbindir}/liveinst
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/zz-liveinst.sh
%{_desktopdir}/liveinst.desktop
%{_iconsdir}/hicolor/*/apps/liveinst.png
%endif

%files gui
%defattr(644,root,root,755)
%{py_sitedir}/pyanaconda/ui/gui

%files tui
%defattr(644,root,root,755)
%{py_sitedir}/pyanaconda/rescue.py[co]
%{py_sitedir}/pyanaconda/text.py[co]
%{py_sitedir}/pyanaconda/ui/tui

%files widgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAnacondaWidgets.so.*.*.*
%ghost %{_libdir}/libAnacondaWidgets.so.2
%{_libdir}/girepository-1.0/AnacondaWidgets-3.0.typelib
%{py_sitedir}/gi/overrides/AnacondaWidgets.py[co]

%files widgets-devel
%defattr(644,root,root,755)
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/AnacondaWidgets
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%defattr(644,root,root,755)
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
#%{_prefix}/libexec/anaconda/dd_*
