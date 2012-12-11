Name:           opengl-games-utils
Version:        0.1
Release:        %mkrel 4
Summary:        Utilities to check proper 3d support before launching 3d games
Group:          Games/Other
License:        Public Domain
URL:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdv2011.0
+ Revision: 613535
- rebuild

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2010.1
+ Revision: 499987
- requires glxinfo instead of mesa-demos

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2010.0
+ Revision: 430209
- rebuild

* Wed Sep 03 2008 Emmanuel Andry <eandry@mandriva.org> 0.1-1mdv2009.0
+ Revision: 279402
- import opengl-games-utils


