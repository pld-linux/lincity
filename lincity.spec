Summary:	LinCity is a city/country simulation game for X and Linux SVGALib. 
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.09
Release:	3
License:	GPL
Group:		X11/Games/Strategy
Group(pl):	X11/Gry/Strategiczne
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/games/%{name}109-src.tar.gz
URL:		http:///www.floot.demon.co.uk/lincity.html
Source1:	lincity.desktop
Patch0:		lincity-1.09-path.patch
Patch1:		lincity-gcc.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 strategy game. You are required to build and maintain a city. You
must feed, house, provide jobs and goods for your residents. You can
build a sustainable economy with the help of renewable energy and
recycling, or you can go for broke and build rockets to escape from a
pollution ridden and resource starved planet, it's up to you. Due to
the finite resources available in any one place, this is not a game
that you can leave for long periods of time.

%description -l pl
Gra strategiczna dla X11. Muisisz wybudowaæ oraz zarz±dzaæ miastem.
Ca³e ¿ycie miasta znajduje siê w twoich rêkach

%prep

%setup -q -n lincity109
%patch0 -p1 
%patch1 -p1 

%build
%{__make} xlincity

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALL=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
install $RPM_SOURCE_DIR/lincity.desktop $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
%{__gzip} -9nf Acknowledgements CHANGES COPYING COPYRIGHT FAQ README \
         README.profiling README.INSTALL 
%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,511)
%attr(511,root,root)%{_prefix}/X11R6/bin/xlincity
%{_libdir}/lincity
%{_sysconfdir}/X11/applnk/Games/lincity.desktop
%doc *.gz
