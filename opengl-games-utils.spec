Name:           opengl-games-utils
Version:        0.2
Release:        1
Summary:        Utilities to check proper 3d support before launching 3d games
Group:          Games/Other
License:        Public Domain
URL:            https://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildArch:      noarch
Requires:       zenity glxinfo

%description
This package contains various shell scripts which are intented for use by
3D games packages. These shell scripts can be used to check if direct rendering
is available before launching an OpenGL game. This package is intended for use
by other packages and is not intended for direct end user use!

%prep
%setup -c -T
cp %{SOURCE2} .

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}


%files
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}
