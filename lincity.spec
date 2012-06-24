#
# Conditional build:
# _without_svgalib - without svgalib support
#
%ifnarch %{ix86} alpha
%define _without_svgalib 1
%endif
Summary:	Lincity is a city/country simulation game for X and Linux SVGALib
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.11
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/games/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.floot.demon.co.uk/lincity.html
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-GCC.patch
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Gra strategiczna dla X11 oraz SVGALib. Trzeba wybudowa� miasto i nim
zarz�dza�. Trzeba karmi� mieszka�c�w, zapewni� im mieszkanie, prac� i
inne dobra. Mo�na stworzy� solidn� gospodark� korzystaj�c z
odnawialnych �r�de� energii i przetw�rstwa odpad�w. Mo�na te� wielkim
wysi�kim zbudowa� rakiety, aby uciec z zanieczyszczonej, pozbawionej
zasob�w planety. Ca�e �ycie miasta znajduje si� w r�kach gracza. Ten
pakiet zawiera pliki wsp�lne dla wersji X11 oraz SVGALib.

%package X11
Summary:	Lincity for X11
Summary(pl):	Lincity dla X11
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}

%description X11
Executable version for X11.

%description X11 -l pl
Program wykonywalny dla X11.

%package SVGALib
Summary:	Lincity for SVGALib
Summary(pl):	Lincity dla SVGALib
Group:		Applications/Games
Requires:	%{name} = %{version}

%description SVGALib
Executable version for SVGALib.

%description SVGALib -l pl}
Program wykonywalny dla SVGALib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
ln -s lincity.man xlincity.man
%{__make} xlincity
%{!?_without_svgalib:%{__make} lincity}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/lincity.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/lincity.png

echo ".so lincity.6" > $RPM_BUILD_ROOT%{_mandir}/man6/xlincity.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Acknowledgements BUGS CHANGES COPYRIGHT FAQ README
%doc README.profiling README.INSTALL
%{_libdir}/games/lincity
%{_mandir}/man6/lincity*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/games/xlincity
%{_applnkdir}/Games/lincity.desktop
%{_pixmapsdir}/lincity.png
%{_mandir}/man6/xlincity*

%if %{?_without_svgalib:0}%{!?_without_svgalib:1}
%files SVGALib
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/games/lincity
%endif
