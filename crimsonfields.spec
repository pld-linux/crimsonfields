Summary:	A hex-based tactical war game
#Summary(pl):	-
Name:		crimsonfields
Version:	0.4.1
Release:	0.1
License:	GPL	
Group:		Games/Strategy
Source0:	http://crimson.seul.org/files/crimson-%{version}.tar.bz2
# Source0-md5:	28cef75cc9a871421cf34ed487921c3f
Patch0:		%{name}-autothingies.patch
URL:		http://crimson.seul.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crimson Fields is a tactical war game in the tradition of Battle Isle for
one or two players.

The outcome of the war lies in your hands. You decide which units are
sent to the front lines, and when to unleash the reserves. Your mission
objectives range from defending strategically vital locations to simply
destroying all enemy forces in the area. Protect supply convoys or raid
enemy facilities to uncover technological secrets or fill your storage
bays so you can repair damaged units or build new ones in your own
factories. Lead your troops to victory!

Tools are available to create custom maps and campaigns. You can also play
the original Battle Isle maps if you have a copy of the game.

#%description -l pl

%prep
%setup -q -n crimson-%{version}
%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%{_datadir}/crimson
%{_mandir}/man*/*
%{_pixmapsdir}/crimson.png
