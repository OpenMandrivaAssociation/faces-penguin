%define	name	faces-penguin
%define	version 0.1
%define	release	%mkrel 8

Summary:	Penguin face icons
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Configuration/Other	
Source0:	%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildArch:	noarch

%description
Penguin faces from previous Mandriva Linux releases.

%prep

%setup -q


%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{_datadir}/mdk/faces
install -m644 olddefault.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 root.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxbaby.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxbox.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxcoocker.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxdad.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxegg.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxgirl.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxhead1.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxhead2.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxmam.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tuxmecano.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 tux.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-brunette-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-curly-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-olddefault-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-girl-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-hat-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-tie-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 user-woman-blond-mdk.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 utildame.png %{buildroot}/%{_datadir}/mdk/faces
install -m644 utilmons.png %{buildroot}/%{_datadir}/mdk/faces

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/mdk/faces/*

