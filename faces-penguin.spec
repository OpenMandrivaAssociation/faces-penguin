%define	name	faces-penguin
%define	version 0.1
%define release	9

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 618253
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2010.0
+ Revision: 428701
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2009.0
+ Revision: 240690
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2008.0
+ Revision: 70214
- use %%mkrel


* Mon Apr 05 2004 Michael Scherer <misc@mandrake.org> 0.1-3mdk
- rebuild.
- remove forbidden word

* Thu Jan 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1-2mdk
- rebuild

* Wed Aug 14 2002 Ben Reser <ben@reser.org> 0.1-1mdk
- resurect the penguins!

