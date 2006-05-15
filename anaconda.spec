Summary:	Graphical system installer
Summary(pl):	Graficzny instalator systemu
Name:		anaconda
Version:	10.89.6
Release:	0.4
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a4fad16ee61ffb268e0bfd6dc76ade12
Source1:	%{name}-mk-images
Source2:	%{name}-upd-instroot
Source3:	%{name}-mk-images.i386
Source4:	%{name}-scrubtree
Patch0:		%{name}-pld.patch
URL:		http://fedora.redhat.com/projects/anaconda-installer/
BuildRequires:	X11-devel
BuildRequires:	beecrypt-devel
BuildRequires:	bogl-bterm >= 0:0.1.9-17
BuildRequires:	bogl-devel >= 0:0.1.9-17
BuildRequires:	bogl-static >= 0:0.1.9-17
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	elfutils-devel
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	glibc-localedb-all
BuildRequires:	glibc-static
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.31.2-3
BuildRequires:	kudzu-devel >= 1.1
BuildRequires:	libselinux-devel >= 1.6
BuildRequires:	newt-devel
BuildRequires:	newt-static
BuildRequires:	pciutils-devel
BuildRequires:	popt-static
BuildRequires:	pump-devel >= 0.8.20
BuildRequires:	python-booty
BuildRequires:	python-devel
BuildRequires:	python-libxml2
BuildRequires:	python-rhpl
BuildRequires:	python-rpm >= 4.2-0.61
BuildRequires:	python-urlgrabber
BuildRequires:	rpm-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	slang-static
BuildRequires:	zlib-devel
BuildRequires:	zlib-static
Requires:	anaconda-help
Requires:	kudzu
Requires:	parted >= 1.6.3-7
Requires:	python-booty
Requires:	python-libxml2
Requires:	python-parted
Requires:	python-rhpl > 0.63
Requires:	python-rhpxl
Requires:	python-rpm >= 4.2-0.61
Requires:	python-urlgrabber
#Requires:	system-logos
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl
Pakiet anaconda zawiera program, którego mo¿na u¿yæ do zainstalowania
systemu. Pliki te maj± niewiele zastosowañ na ju¿ zainstalowanym
systemie.

%package runtime
Summary:	Graphical system installer portions needed only for fresh installs
Summary(pl):	Elementy graficznego instalatora systemu potrzebne tylko przy nowych instalacjach
Group:		Applications/System
AutoReqProv:	false
Requires:	python
Requires:	python-libxml2
Requires:	python-rpm >= 4.2-0.61

%description runtime
The anaconda-runtime package contains parts of the installation system
which are needed for installing new systems. These files are used to
build media sets, but are not meant for use on already installed
systems.

%description runtime -l pl
Pakiet anaconda-runtime zawiera elementy instalatora potrzebne tylko
do instalowania nowych systemów. Pliki te s³u¿± do tworzenia zestawu
no¶ników, nie s± przewidziane do u¿ywania na ju¿ zainstalowanych
systemach.

%prep
%setup -q
%patch0 -p1

rm -f po/no.po
mv -f po/{eu_ES,eu}.po
mv -f po/{sr,sr@Latn}.po

sed -i -e 's/$(PYTHON) scripts/python scripts/' Makefile
cp %{SOURCE1} scripts/mk-images
cp %{SOURCE2} scripts/upd-instroot
cp %{SOURCE3} scripts/mk-images.i386
cp %{SOURCE4} scripts/scrubtree

%build
# locale check
if [ "$(locale -a | grep -c en_US.utf8)" = 0 ]; then
	echo >&2 "en_US.utf8 locale not available. build will fail!"
	echo >&2 "Install glibc-localedb-all or compile it!"
	exit 1
fi

%{__make} depend
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/command-line.txt
%doc docs/install-methods.txt
%doc docs/kickstart-docs.txt
%doc docs/mediacheck.txt
%doc docs/anaconda-release-notes.txt
%attr(755,root,root) %{_bindir}/mini-wm
%attr(755,root,root) %{_sbindir}/anaconda
%{_datadir}/anaconda
%{_libdir}/anaconda

%files runtime
%defattr(644,root,root,755)
%dir %{_libdir}/anaconda-runtime
%dir %attr(755,root,root) %{_libdir}/anaconda-runtime/boot
%attr(755,root,root) %{_libdir}/anaconda-runtime/boot/syslinux.cfg
%{_libdir}/anaconda-runtime/boot/boot.msg
%{_libdir}/anaconda-runtime/boot/general.msg
%{_libdir}/anaconda-runtime/boot/options.msg
%{_libdir}/anaconda-runtime/boot/param.msg
%{_libdir}/anaconda-runtime/boot/rescue.msg
%{_libdir}/anaconda-runtime/boot/snake.msg
%attr(755,root,root) %{_libdir}/anaconda-runtime/buildinstall
%attr(755,root,root) %{_libdir}/anaconda-runtime/checkisomd5
%attr(755,root,root) %{_libdir}/anaconda-runtime/filtermoddeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/fixmtime.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/genhdlist
%attr(755,root,root) %{_libdir}/anaconda-runtime/getkeymaps
%attr(755,root,root) %{_libdir}/anaconda-runtime/implantisomd5
%attr(755,root,root) %{_libdir}/anaconda-runtime/libunicode-lite.so.1
%dir %attr(755,root,root) %{_libdir}/anaconda-runtime/loader
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/init
%attr(755,root,root) %{_libdir}/anaconda-runtime/loader/loader
%{_libdir}/anaconda-runtime/loader/font.bgf.gz
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
%attr(755,root,root) %{_libdir}/anaconda-runtime/mk-rescueimage.x86_64
%attr(755,root,root) %{_libdir}/anaconda-runtime/moddeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/modlist
%attr(755,root,root) %{_libdir}/anaconda-runtime/pkgorder
%attr(755,root,root) %{_libdir}/anaconda-runtime/pyisomd5sum.so
%attr(755,root,root) %{_libdir}/anaconda-runtime/pythondeps
%attr(755,root,root) %{_libdir}/anaconda-runtime/readmap
%attr(755,root,root) %{_libdir}/anaconda-runtime/scrubtree
%{_libdir}/anaconda-runtime/screenfont-i386.gz
%attr(755,root,root) %{_libdir}/anaconda-runtime/splittree.py
%attr(755,root,root) %{_libdir}/anaconda-runtime/trimmodalias
%attr(755,root,root) %{_libdir}/anaconda-runtime/trimpciids
%attr(755,root,root) %{_libdir}/anaconda-runtime/upd-instroot
%attr(755,root,root) %{_libdir}/anaconda-runtime/yumcache
