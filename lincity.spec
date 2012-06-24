#
# Conditional build:
%bcond_without	svga	# without svgalib support
#
Summary:	Lincity is a city/country simulation game for X11 and Linux SVGALib
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.13.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/lincity/%{name}-%{version}.tar.gz
# Source0-md5:	2d37906d4b141cd457ec93d778bb8fe1
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://lincity.sourceforge.net/
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
Gra strategiczna dla X11 oraz SVGALib. Trzeba wybudowa� miasto i nim
zarz�dza�. Trzeba karmi� mieszka�c�w, zapewni� im mieszkanie, prac� i
inne dobra. Mo�na stworzy� solidn� gospodark� korzystaj�c z odnawialnych 
�r�de� energii i przetw�rstwa odpad�w. Mo�na te� wielkim wysi�kiem 
zbudowa� rakiety, aby uciec z zanieczyszczonej, pozbawionej zasob�w 
planety. Ca�e �ycie miasta znajduje si� w r�kach gracza. Ten pakiet 
zawiera pliki wsp�lne dla wersji X11 oraz SVGALib.

%package X11
Summary:	Lincity for X11
Summary(pl):	Lincity dla X11
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}

%description X11
Executable version for X11.

%description X11 -l pl
Program wykonywalny dla X11.

%package svga
Summary:	Lincity for SVGALib
Summary(pl):	Lincity dla SVGALib
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/lincity.desktop
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
%{_desktopdir}/lincity.desktop
%{_pixmapsdir}/lincity.png
%{_mandir}/man?/xlincity*

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lincity
%endif
