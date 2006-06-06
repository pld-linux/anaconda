# TODO
# - kill /mnt/runtime symlink hacks (leave the host alone!)
#
%if 0
# FC to PLD deps replace rules, extracted from cvs logs
:%s#libxml2-python#python-libxml2#
:%s#pyparted#python-parted#
:%s#booty#python-booty#
:%s#rhpl#python-rhpl#
:%s#rhpxl#python-rhpxl#
:%s#rpm-python#python-rpm#
:%s#gtk2-devel#gtk+2-devel#
:%s#pykickstart#python-kickstart#
:%s#squashfs-tools#squashfs#
%endif
Summary:	Graphical system installer
Summary(pl):	Graficzny instalator systemu
Name:		anaconda
Version:	11.0.5
Release:	0.78
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	f814e7d0011dd44c3c3cf12b6ddb5b40
Source1:	%{name}-mk-images
Source2:	%{name}-upd-instroot
Source3:	%{name}-mk-images.i386
Source4:	%{name}-scrubtree
Source5:	%{name}-installclass-pld.py
Source6:	%{name}-splash.png
# Source6-md5:	6b38a868585adfd3a96a4ad16973c1f8
Patch0:		%{name}-pld.patch
Patch1:		%{name}-BUS_XEN.patch
Patch2:		%{name}-vserver-proc.patch
Patch3:		%{name}-pkgorder.patch
Patch4:		%{name}-errorhandling.patch
Patch5:		%{name}-libdir.patch
Patch6:		%{name}-pld-release.patch
Patch7:		%{name}-timezone.patch
Patch8:		%{name}-kernel.patch
Patch9:		%{name}-optflags.patch
Patch10:	%{name}-network.patch
Patch11:	%{name}-branding.patch
Patch12:	%{name}-x11.patch
Patch13:	%{name}-installclasses.patch
Patch14:	%{name}-release_notes_viewer_gui.patch
URL:		http://fedora.redhat.com/projects/anaconda-installer/
BuildRequires:	bzip2-devel
BuildRequires:	device-mapper-static >= 1.01.05
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	glibc-static
BuildRequires:	gtk+2-devel
BuildRequires:	kudzu-devel >= 1.2.0
BuildRequires:	libselinux-static >= 1.6
BuildRequires:	libsepol-static
BuildRequires:	newt-static
BuildRequires:	popt-static
BuildRequires:	pump-static >= 0.8.24-1
BuildRequires:	python-devel
BuildRequires:	python-rhpl
BuildRequires:	python-rpm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	sed >= 4.0
BuildRequires:	slang-static
BuildRequires:	zlib-static
Requires:	/etc/pld-release
Requires:	device-mapper >= 1.01.05
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	glibc-localedb-all
Requires:	grubby
Requires:	hfsutils
Requires:	jfsutils
Requires:	kudzu > 1.2.0
Requires:	lvm2
Requires:	mdadm
Requires:	python-booty >= 0.71-0.6
Requires:	python-devel-tools
Requires:	python-kickstart
Requires:	python-libxml2
Requires:	python-parted
Requires:	python-rhpl >= 0.176-1.1
Requires:	python-rpm >= 4.2-0.61
Requires:	python-snack
Requires:	python-urlgrabber >= 2.9.8
Requires:	reiserfsprogs
Requires:	xfsprogs
Requires:	yum >= 2.5.1-3
%ifnarch s390 s390x
Requires:	python-pyblock >= 0.7-1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl
Pakiet anaconda zawiera program, kt�rego mo�na u�y� do zainstalowania
systemu. Pliki te maj� niewiele zastosowa� na ju� zainstalowanym
systemie.

%package gui
Summary:	Anaconda GTK+2 GUI
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	X11-OpenGL-core
Requires:	X11-Xserver
Requires:	X11-fonts
Requires:	pirut
Requires:	python-gnome-canvas
Requires:	system-config-keyboard
#Requires:	system-logos
Requires:	vnc-utils
%ifnarch s390 s390x ppc64
Requires:	python-rhpxl >= 0.18-0.6
%endif

%description gui
Anaconda GUI portion.

%package runtime
Summary:	Graphical system installer portions needed only for fresh installs
Summary(pl):	Elementy graficznego instalatora systemu potrzebne tylko przy nowych instalacjach
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

%description runtime -l pl
Pakiet anaconda-runtime zawiera elementy instalatora potrzebne tylko
do instalowania nowych system�w. Pliki te s�u�� do tworzenia zestawu
no�nik�w, nie s� przewidziane do u�ywania na ju� zainstalowanych
systemach.

%package debug
Summary:	Sourcecode for Anaconda
Summary(pl):	Kod �r�d�owy Anacondy
Group:		Applications/System
AutoReqProv:	false
Requires:	%{name} = %{version}-%{release}

%description debug
Anaconda sourcecode for debugging purposes.

%description debug -l pl
Kod �r�d�owy Anacondy do cel�w diagnostycznych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

rm -f po/no.po
mv -f po/{eu_ES,eu}.po

# we don't want this being visible, neither want we to kill it (the
# other's aren't valid anyway (outdated probably).
mv installclasses/fedora.py{,.orig}
# we want this install class ;)
cp %{SOURCE5} installclasses/pld.py

sed -i -e 's/$(PYTHON) scripts/python scripts/' Makefile

%build
# locale check
if [ "$(locale -a | grep -c en_US.utf8)" = 0 ]; then
	echo >&2 "en_US.utf8 locale not available. build will fail!"
	echo >&2 "Install glibc-localedb-all or compile it!"
	exit 1
fi

%{__make} depend -j1 \
	CC="%{__cc}"

%{__make} -j1 \
	CC="%{__cc}" \
	REALCC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

./py-compile isys/isys.py

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install isys/isys.py[co] $RPM_BUILD_ROOT%{_libdir}/anaconda

cp %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/anaconda-runtime/mk-images
cp %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/anaconda-runtime/upd-instroot
cp %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/anaconda-runtime/mk-images.i386
cp %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/anaconda-runtime/scrubtree
cp %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/anaconda/splash.png

%find_lang %{name}

# hack so py_postclean would preserve it
install $RPM_BUILD_ROOT%{_libdir}/anaconda/iw/release_notes_viewer_gui{.py,}

%{!?debug:%py_postclean %{_libdir}/anaconda}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_sbindir}/anaconda
%dir %{_libdir}/anaconda
%{_libdir}/anaconda/*.py[co]
%exclude %{_libdir}/anaconda/xsetup.py[co]
%dir %{_libdir}/anaconda/installclasses
%{_libdir}/anaconda/installclasses/*.py[co]
%dir %{_libdir}/anaconda/textw
%{_libdir}/anaconda/textw/*.py[co]
%{_libdir}/anaconda/lang-names
%{_libdir}/anaconda/lang-table
%{_libdir}/anaconda/lang-table-kon
%attr(755,root,root) %{_libdir}/anaconda/_isys.so

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mini-wm
%attr(755,root,root) %{_libdir}/anaconda/iw/release_notes_viewer_gui
%attr(755,root,root) %{_libdir}/anaconda/xmouse.so
%attr(755,root,root) %{_libdir}/anaconda/xutils.so
%{_libdir}/anaconda/xsetup.py[co]
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
%dir %attr(755,root,root) %{_libdir}/anaconda-runtime/boot
%attr(755,root,root) %{_libdir}/anaconda-runtime/boot/syslinux.cfg
%{_libdir}/anaconda-runtime/boot/boot.msg
%{_libdir}/anaconda-runtime/boot/general.msg
%{_libdir}/anaconda-runtime/boot/options.msg
%{_libdir}/anaconda-runtime/boot/param.msg
%{_libdir}/anaconda-runtime/boot/rescue.msg
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall
%attr(755,root,root) %{_libdir}/anaconda-runtime/checkisomd5
%attr(755,root,root) %{_libdir}/anaconda-runtime/filtermoddeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/fixmtime.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/getkeymaps
%attr(755,root,root) %{_libdir}/anaconda-runtime/implantisomd5
%{_libdir}/anaconda-runtime/keymaps-override-*
%attr(755,root,root) %{_libdir}/anaconda-runtime/libunicode-lite.so.1
%dir %attr(755,root,root) %{_libdir}/anaconda-runtime/loader
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/init
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/loader
%{_libdir}/anaconda-runtime/loader/loader.tr
%{_libdir}/anaconda-runtime/loader/module-info
%{_libdir}/anaconda-runtime/loader/unicode-linedraw-chars.txt
%attr(755,root,root) %{_libdir}/anaconda-runtime/makestamp.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/mapshdr
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.i386
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.ia64
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.ppc
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.s390
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-images.x86_64
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-rescueimage.i386
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-rescueimage.ppc
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-rescueimage.x86_64
%attr(755,root,root) %{_libdir}/anaconda-runtime/moddeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/modlist
%attr(755,root,root) %{_libdir}/anaconda-runtime/pkgorder
%attr(755,root,root) %{_libdir}/anaconda-runtime/pyisomd5sum.so
%attr(755,root,root) %{_libdir}/anaconda-runtime/pyrc.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/pythondeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/readmap
%attr(755,root,root) %{_libdir}/anaconda-runtime/scrubtree
%{_libdir}/anaconda-runtime/screenfont-*.gz
%attr(755,root,root) %{_libdir}/anaconda-runtime/splittree.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/trimmodalias
%attr(755,root,root) %{_libdir}/anaconda-runtime/trimpciids
%attr(755,root,root) %{_libdir}/anaconda-runtime/upd-instroot
%attr(755,root,root) %{_libdir}/anaconda-runtime/yumcache
