#
# Conditional build:
# _without_svgalib - without svgalib support
#
%ifnarch %{ix86} alpha
%define _without_svgalib 1
%endif
Summary:	LinCity is a city/country simulation game for X and Linux SVGALib
Summary(pl):	Lincity jest symulatorem miasta/kraju dla X11 oraz SVGALib
Name:		lincity
Version:	1.11
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/games/%{name}-%{version}.tar.gz
URL:		http://www.floot.demon.co.uk/lincity.html
Source1:	%{name}.desktop
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
Gra strategiczna dla X11 oraz SVGALib. Trzeba wybudowaæ i zarz±dzaæ
miastem. Trzeba karmiæ, budowaæ, zapewniæ pracê i inne dobra dla
mieszkañców. Mo¿na stworzyæ wytrzyma³± gospodarkê z pomoc±
odnawialnych ¼róde³ energii i recyclingu, mo¿na te¿ niszczyæ i budowaæ
rakiety, aby uciec z zanieczyszczonej planety wyczyszczonej z zasobów.
Ca³e ¿ycie miasta znajduje siê w rêkach gracza. Ten pakiet zawiera
pliki wspólne dla wersji X11 oraz SVGALib.

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
%{!?no_svgalib:%{__make} lincity}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
install $RPM_SOURCE_DIR/lincity.desktop $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games

echo ".so lincity.6" > $RPM_BUILD_ROOT%{_mandir}/man6/xlincity.6

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc Acknowledgements BUGS CHANGES COPYING COPYRIGHT FAQ README
%doc README.profiling README.INSTALL
%{_libdir}/games/lincity
%{_sysconfdir}/X11/applnk/Games/lincity.desktop
%{_mandir}/man6/lincity*

%files X11
%defattr(644,root,root,755)
%attr(511,root,root)%{_prefix}/games/xlincity
%{_mandir}/man6/xlincity*

%if %{?_without_svgalib:0}%{!?_without_svgalib:1}
%files SVGALib
%defattr(644,root,root,755)
%attr(511,root,root)%{_prefix}/games/lincity
%endif
