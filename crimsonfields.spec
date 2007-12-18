#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
%bcond_without	SDL_net		# build without SDL_net
#
Summary:	A hex-based tactical war game
Summary(pl.UTF-8):	Taktyczna gra wojenna oparta na hex
Name:		crimsonfields
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://crimson.seul.org/files/crimson-%{version}.tar.bz2
# Source0-md5:	a6024dd95c8767cee9907475bf827291
Patch0:		%{name}-autothingies.patch
Patch1:		%{name}-desktop.patch
URL:		http://crimson.seul.org/
BuildRequires:	SDL-devel >= 1.1.5
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel}
%{?with_SDL_net:BuildRequires:	SDL_net-devel >= 1.2.6}
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crimson Fields is a tactical war game in the tradition of Battle Isle
for one or two players.

The outcome of the war lies in your hands. You decide which units are
sent to the front lines, and when to unleash the reserves. Your
mission objectives range from defending strategically vital locations
to simply destroying all enemy forces in the area. Protect supply
convoys or raid enemy facilities to uncover technological secrets or
fill your storage bays so you can repair damaged units or build new
ones in your own factories. Lead your troops to victory!

Tools are available to create custom maps and campaigns. You can also
play the original Battle Isle maps if you have a copy of the game.

%description -l pl.UTF-8
Crimson Fields to taktyczna gra wojenna dla jednego lub dwóch graczy,
utrzymana w tradycji Battle Isle.

Wynik gry leży w Twoich rękach. Ty decydujesz, które jednostki są
wysyłane na linie frontu i kiedy wypuścić rezerwę. Cele misji
rozciągają się od obrony strategicznych miejsc po zwykłe zniszczenie
wszystkich sił wroga w terenie. Zabezpiecz konwoje dostawcze albo
najedź na wroga, aby odkryć jego sekrety technologiczne lub uzupełnić
swoje zapasy, co umożliwi naprawę uszkodzonych jednostek albo
zbudowanie nowych we własnych fabrykach. Prowadź swoje wojsko do
zwycięstwa!

Dostępne są narzędzia do tworzenia własnych map i kampanii. Można
także grać na oryginalnych mapach Battle Isle, jeśli mamy kopię gry.

%prep
%setup -q -n crimson-%{version}
%patch0 -p1
%patch1 -p1

%build
cp %{_datadir}/automake/config.sub config/.
cp %{_datadir}/automake/config.guess config/.
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-cfed \
	--enable-bi2cf \
	--enable-comet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/crimson
%{_datadir}/crimson/*.ttf
%{_datadir}/crimson/cf.dat
%{_datadir}/crimson/default.*
%{_datadir}/crimson/*.bmp
%{_datadir}/crimson/levels
%dir %{_datadir}/crimson/locale
%lang(de) %{_datadir}/crimson/locale/de.dat
%lang(fr) %{_datadir}/crimson/locale/fr.dat
%lang(en) %{_datadir}/crimson/locale/en.dat
%lang(hu) %{_datadir}/crimson/locale/hu.dat
%lang(it) %{_datadir}/crimson/locale/it.dat
%lang(pl) %{_datadir}/crimson/locale/pl.dat
%lang(sk) %{_datadir}/crimson/locale/sk.dat
%lang(sr) %{_datadir}/crimson/locale/sr.dat
%{_datadir}/crimson/music
%{_datadir}/crimson/sound
%{_desktopdir}/*.desktop
%{_mandir}/man*/*
%{_pixmapsdir}/crimson.png
