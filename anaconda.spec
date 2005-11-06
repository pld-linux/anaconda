Summary:	Graphical system installer
Summary(pl):	Graficzny instalator systemu
Name:		anaconda
Version:	10.89.6
Release:	0.1
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
Requires:	system-logos
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda package contains the program which can be used to install
system. These files are of little use on an already installed system.

%description -l pl
Pakiet anaconda zawiera program, kt�rego mo�na u�y� do zainstalowania
systemu. Pliki te maj� niewiele zastosowa� na ju� zainstalowanym
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
do instalowania nowych system�w. Pliki te s�u�� do tworzenia zestawu
no�nik�w, nie s� przewidziane do u�ywania na ju� zainstalowanych
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
%defattr(-,root,root,755)
%{_libdir}/anaconda-runtime

%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: anaconda.spec,v $
Revision 1.8  2005-11-06 16:54:15  patrys
- added R: python-rhpxl

Revision 1.7  2005/11/06 15:53:49  patrys
- up to 10.89.6

Revision 1.6  2005/10/31 19:29:58  glen
- BR bogl-static
- utf-8 locale check for build

Revision 1.5  2005/05/03 18:03:18  patrys
- updated

Revision 1.4  2005/04/29 16:38:04  qboosh
- locales cleanup

Revision 1.3  2005/04/29 16:22:41  qboosh
- pl, some cleanups

Revision 1.2  2005/04/28 22:45:31  patrys
- moved from DEVEL

Revision 1.1.2.7  2005/04/23 23:35:46  patrys
- fixed deps

Revision 1.1.2.6  2005/04/23 22:51:30  patrys
- fixed deps

Revision 1.1.2.5  2005/04/23 21:35:57  patrys
- fixed deps

Revision 1.1.2.4  2005/04/23 18:14:22  patrys
- working version codenamed "hangover"

Revision 1.1.2.3  2005/04/23 17:59:29  patrys
- more fixes, builds now

Revision 1.1.2.2  2005/04/23 17:20:19  patrys
- add static requirements for glibc and zlib

Revision 1.1.2.1  2005/04/23 16:49:50  patrys
- Initial PLD release
- missing deps
- something wrong with glibc dependency (ld is unable to find -lresolv)
