Summary:	LinCity is a city/country simulation game for X and Linux SVGALib. 
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/games/%{name}-%{version}.tar.gz
URL:		http:///www.floot.demon.co.uk/lincity.html
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-GCC.patch
%{!?no_svgalib:BuildRequires:	svgalib}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 and SVGALib strategy game. You are required to build and maintain
a city. You must feed, house, provide jobs and goods for your
residents. You can build a sustainable economy with the help of
renewable energy and recycling, or you can go for broke and build
rockets to escape from a pollution ridden and resource starved planet,
it's up to you. Due to the finite resources available in any one
place, this is not a game that you can leave for long periods of time.
Shared files for X11 and SVGALib.

%description -l pl
Gra strategiczna dla X11 oraz SVGALib. Muisisz wybudowa� oraz
zarz�dza� miastem. Ca�e �ycie miasta znajduje si� w twoich r�kach.
Pliki wsp�lne dla wersji dla X11 oraz dla SVGALib.

%package X11
Summary:	Lincity for X11
Summary(pl):	Lincity dla X11
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}

%description X11
Executable version for X11.

%description X11 -l pl
Program wykonywalny dla X11.

%{!?no_svgalib:%package SVGALib}
%{!?no_svgalib:Summary:	Lincity for SVGALib}
%{!?no_svgalib:Summary(pl):	Lincity dla SVGALib}
%{!?no_svgalib:Group:		Applications/Games}
%{!?no_svgalib:Group(de):	Applikationen/Spiele}
%{!?no_svgalib:Group(pl):	Aplikacje/Gry}
%{!?no_svgalib:Requires:	%{name} = %{version}}

%{!?no_svgalib:%description SVGALib}
%{!?no_svgalib:Executable version for SVGALib.}

%{!?no_svgalib:%description SVGALib -l pl}
%{!?no_svgalib:Program wykonywalny dla SVGALib.}

%prep

%setup -q 
%patch0 -p1 
%patch1 -p1 

%build
%{__make} xlincity
%{!?no_svgalib:%{__make} lincity}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
install $RPM_SOURCE_DIR/lincity.desktop $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
gzip -9nf Acknowledgements BUGS CHANGES COPYING COPYRIGHT FAQ README \
         README.profiling README.INSTALL 

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_libdir}/games/lincity
%{_sysconfdir}/X11/applnk/Games/lincity.desktop
%{_mandir}/man6/*
%doc *.gz

%files X11
%defattr(644,root,root,755)
%attr(511,root,root)%{_prefix}/games/xlincity

%{!?no_svgalib:%files SVGALib}
%{!?no_svgalib:%defattr(644,root,root,755)}
%{!?no_svgalib:%attr(511,root,root)%{_prefix}/games/lincity}
