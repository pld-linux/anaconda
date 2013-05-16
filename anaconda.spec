# TODO
# - code poldek backend (python-poldek pkg exists!)

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define gettextver 0.11
%define gconfversion 2.28.1
%define intltoolver 0.31.2-3
%define libnlver 1.0
%define pykickstartver 1.99.30
%define yumver 3.4.3-7
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define nmver 1:0.7.1-3.git20090414
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.23-1
%define sckeyboardver 1.3.1
%define firewalldver 0.2.9-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 024-25
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 2.0-0.870.3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define libselinuxver 2.1
Summary:	Graphical system installer
Summary(pl.UTF-8):	Graficzny instalator systemu
Name:		anaconda
Version:	19.25
Release:	0.5
License:	GPL
Group:		Applications/System
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/anaconda/%{name}-%{version}.tar.bz2/b3f242b630aa1d4a458756b5816a0603/anaconda-%{version}.tar.bz2
# Source0-md5:	b3f242b630aa1d4a458756b5816a0603
URL:		http://fedoraproject.org/wiki/Anaconda
BuildRequires:	NetworkManager-devel >= %{nmver}
BuildRequires:	audit-libs-devel
BuildRequires:	dbus-devel >= %{dbusver}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext >= %{gettextver}
BuildRequires:	glade-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool >= %{intltoolver}
BuildRequires:	libarchive-devel >= %{libarchivever}
BuildRequires:	libgnomekbd-devel
BuildRequires:	libnl-devel >= %{libnlver}
BuildRequires:	libxklavier-devel
BuildRequires:	pango-devel
BuildRequires:	python-dbus
BuildRequires:	python-devel
BuildRequires:	python-nose
BuildRequires:	python-pygobject3
BuildRequires:	python-pykickstart >= %{pykickstartver}
BuildRequires:	python-urlgrabber >= %{pythonurlgrabberver}
BuildRequires:	rpm-devel >= %{rpmver}
BuildRequires:	systemd-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	yum >= %{yumver}
Requires:	GConf2 >= %{gconfversion}
Requires:	NetworkManager >= %{nmver}
Requires:	anaconda-widgets = %{version}-%{release}
Requires:	anaconda-yum-plugins
Requires:	authconfig
Requires:	chrony
Requires:	desktop-file-utils
Requires:	dhclient
Requires:	firewalld >= %{firewalldver}
Requires:	gnome-icon-theme-symbolic
Requires:	hostname
Requires:	isomd5sum >= %{isomd5sum}
Requires:	kbd
Requires:	libgnomekbd
Requires:	libreport-anaconda >= 2.0.21-1
Requires:	libuser-python
Requires:	libxklavier
Requires:	nm-connection-editor
Requires:	ntpdate
Requires:	open-iscsi >= %{iscsiver}
Requires:	parted >= %{partedver}
Requires:	pyparted >= %{pypartedver}
Requires:	python-IPy
Requires:	python-babel
Requires:	python-blivet >= 0.12
Requires:	python-bugzilla
Requires:	python-dbus
Requires:	python-meh >= %{mehver}
Requires:	python-nss
Requires:	python-pwquality
Requires:	python-pykickstart >= %{pykickstartver}
Requires:	python-pytz
Requires:	python-rpm >= %{rpmpythonver}
Requires:	python-selinux
Requires:	python-selinux >= %{libselinuxver}
Requires:	python-urlgrabber >= %{pythonurlgrabberver}
Requires:	rsync
Requires:	system-logos
Requires:	tigervnc-server-minimal
Requires:	usermode
Requires:	util-linux >= %{utillinuxver}
Requires:	yum >= %{yumver}
Requires:	yum-utils >= %{yumutilsver}
Requires:	zenity
%ifarch %{ix86} %{x8664} ia64
Requires:	dmidecode
Requires:	hfsplus-tools
%endif
Obsoletes:	anaconda-images <= 10
Obsoletes:	anaconda-runtime < %{version}-%{release}
Obsoletes:	booty <= 0.107-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl.UTF-8
Pakiet anaconda zawiera program, którego można użyć do zainstalowania
systemu. Pliki te mają niewiele zastosowań na już zainstalowanym
systemie.

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

# / on /usr kicks in
%{__sed} -i -e '1 s,#!/usr/bin/bash,#!/bin/sh,' scripts/run-anaconda

# TODO: rpm5 porting
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

# unsupported locales
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bal
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/eu_ES
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ilo

find $RPM_BUILD_ROOT -type f -name "*.la" | xargs %{__rm} -v

desktop-file-install ---dir=$RPM_BUILD_ROOT%{_desktopdir} $RPM_BUILD_ROOT%{_desktopdir}/liveinst.desktop

%find_lang %{name}

%{!?debug:%py_postclean %{_libdir}/anaconda}

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database

%postun
update-desktop-database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/{command-line,install-methods,mediacheck}.txt
%{systemdunitdir}/*
%{systemdunitdir}-generators/*
%attr(755,root,root) %{_bindir}/anaconda-cleanup
%attr(755,root,root) %{_bindir}/analog
%attr(755,root,root) %{_bindir}/instperf
%attr(755,root,root) %{_sbindir}/anaconda
%attr(755,root,root) %{_sbindir}/handle-sshpw
%attr(755,root,root) %{_sbindir}/logpicker
%{_datadir}/anaconda
%exclude %{_datadir}/anaconda/tzmapdata/*
%{_libdir}/anaconda
%{py_sitedir}/pyanaconda
%{py_sitedir}/log_picker

# live
%attr(755,root,root) %{_bindir}/liveinst
%attr(755,root,root) %{_sbindir}/liveinst
%config(noreplace) /etc/pam.d/*
%config(noreplace) /etc/security/console.apps/*
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*

%files widgets
%defattr(644,root,root,755)
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{_libdir}/python*/site-packages/gi/overrides/*
%{_datadir}/anaconda/tzmapdata/*

%files widgets-devel
%defattr(644,root,root,755)
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%defattr(644,root,root,755)
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
#%{_prefix}/libexec/anaconda/dd_*
