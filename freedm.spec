Name:		freedm
Summary:	Deathmatch Doom Game with no monsters
Version:	0.12.1
Release:	1
Source0:	https://github.com/freedoom/freedoom/releases/download/v%{version}/%{name}-%{version}.zip
License:	GPLv2
Group:		Games/Shooter
Url:		http://freedoom.github.io/
BuildArch:	noarch
Provides:	doom-iwad
Requires:	doom-engine

%description
FreeDM is a fast-paced competitive deathmatch game, part of the Freedoom project. 
Rather than the usual single-player focused levels, these contain no monsters and
are intended for deathmatch only.

%prep
%setup -q

%build

%install
install -D -m644 %{name}.wad %{buildroot}%{_gamesdatadir}/doom/%{name}.wad

%files
%doc CREDITS.txt README.html NEWS.html freedoom-manual.pdf
%license COPYING.txt
%{_gamesdatadir}/doom/%{name}.wad
