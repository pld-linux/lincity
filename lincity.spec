#
# Conditional build:
%bcond_without	svga	# with svgalib support
#
%ifnarch %{ix86} alpha
%undefine with_svga
%endif
Summary:	Lincity is a city/country simulation game for X11 and Linux SVGALib
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.12.0
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/lincity/%{name}-%{version}.tar.gz
# Source0-md5:	98daeef749d3ec17208193b6a1dc6b03
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://lincity.sourceforge.net/
#Patch0:		%{name}-DESTDIR.patch
#Patch1:		%{name}-GCC.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 and SVGALib strategy game. You are required to build and maintain
a city. You must feed, house, provide jobs and goods for your
residents. You can build a sustainable economy with the help of
renewable energy and recycling, or you can go for broke and build
rockets to escape from a pollution ridden and resource starved planet,
it's up to you. Due to the finite resources available in any one
place, this is not a game that you can leave for long periods of time.
This package contains shared files for X11 and SVGALib.

%description -l pl
Gra strategiczna dla X11 oraz SVGALib. Trzeba wybudowaæ miasto i nim
zarz±dzaæ. Trzeba karmiæ mieszkañców, zapewniæ im mieszkanie, pracê i
inne dobra. Mo¿na stworzyæ solidn± gospodarkê korzystaj±c z
odnawialnych ¼róde³ energii i przetwórstwa odpadów. Mo¿na te¿ wielkim
wysi³kim zbudowaæ rakiety, aby uciec z zanieczyszczonej, pozbawionej
zasobów planety. Ca³e ¿ycie miasta znajduje siê w rêkach gracza. Ten
pakiet zawiera pliki wspólne dla wersji X11 oraz SVGALib.

%package X11
Summary:	Lincity for X11
Summary(pl):	Lincity dla X11
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}

%description X11
Executable version for X11.

%description X11 -l pl
Program wykonywalny dla X11.

%package svga
Summary:	Lincity for SVGALib
Summary(pl):	Lincity dla SVGALib
Group:		Applications/Games
Requires:	%{name} = %{version}

%description svga
Executable version for SVGALib.

%description svga -l pl
Program wykonywalny dla SVGALib.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy/lincity.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/lincity.png

echo ".so lincity.6" > $RPM_BUILD_ROOT%{_mandir}/man6/xlincity.6
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Acknowledgements CHANGES COPYRIGHT README* TODO
%{_datadir}/%{name}
%{_mandir}/man?/lincity*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xlincity
%{_applnkdir}/Games/Strategy/lincity.desktop
%{_pixmapsdir}/lincity.png
%{_mandir}/man?/xlincity*

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lincity
%endif
