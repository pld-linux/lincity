Summary:	LinCity is a city/country simulation game for X and Linux SVGALib. 
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/games/%{name}-%{version}.tar.gz
URL:		http:///www.floot.demon.co.uk/lincity.html
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-GCC.patch
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
Gra strategiczna dla X11 oraz SVGALib. Muisisz wybudowaæ oraz
zarz±dzaæ miastem. Ca³e ¿ycie miasta znajduje siê w twoich rêkach.
Pliki wspólne dla wersji dla X11 oraz dla SVGALib.

%package X11
Summary:	Lincity for X11
Summary(pl):	Lincity dla X11
Group:		X11/Applications/Games/Strategy
Group(de):	X11/Applications/Spiele/Strategie
Group(pl):	X11/Aplikacje/Gry/Strategiczne
Requires:	%{name} = %{version}

%description X11
Executable version for X11.

%description X11 -l pl
Program wykonywalny dla X11.

%package SVGALib
Summary:	Lincity for SVGALib
Summary(pl):	Lincity dla SVGALib
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	%{name} = %{version}

%description SVGALib
Executable version for SVGALib.

%description SVGALib -l pl
Program wykonywalny dla SVGALib.

%prep

%setup -q 
%patch0 -p1 
%patch1 -p1 

%build
%{__make} xlincity
%{__make} lincity

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

%files SVGALib
%defattr(644,root,root,755)
%attr(511,root,root)%{_prefix}/games/lincity
