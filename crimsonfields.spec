#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
%bcond_without	SDL_net		# build without SDL_net
#
Summary:	A hex-based tactical war game
Summary(pl):	Taktyczna gra wojenna oparta na hex
Name:		crimsonfields
Version:	0.5.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://crimson.seul.org/files/crimson-%{version}.tar.bz2
# Source0-md5:	71d5137ede548a2108198acac44d3ab4
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

%description -l pl
Crimson Fields to taktyczna gra wojenna dla jednego lub dwóch graczy,
utrzymana w tradycji Battle Isle.

Wynik gry le¿y w Twoich rêkach. Ty decydujesz, które jednostki s±
wysy³ane na linie frontu i kiedy wypu¶ciæ rezerwê. Cele misji
rozci±gaj± siê od obrony strategicznych miejsc po zwyk³e zniszczenie
wszystkich si³ wroga w terenie. Zabezpiecz konwoje dostawcze albo
najed¼ na wroga, aby odkryæ jego sekrety technologiczne lub uzupe³niæ
swoje zapasy, co umo¿liwi naprawê uszkodzonych jednostek albo
zbudowanie nowych we w³asnych fabrykach. Prowad¼ swoje wojsko do
zwyciêstwa!

Dostêpne s± narzêdzia do tworzenia w³asnych map i kampanii. Mo¿na
tak¿e graæ na oryginalnych mapach Battle Isle, je¶li mamy kopiê gry.

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
