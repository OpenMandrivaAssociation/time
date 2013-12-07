Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.7
Release:	43
License:	GPL
Group:		Monitoring
URL:		http://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.bz2
Patch0:		time-1.7.info.patch
Patch1:		time-1.7-ressource.patch
Patch2:		time-1.7-quiet.1.patch
Patch3:		time-1.7-fixinfo.patch
Patch4:		time-1.7-build.patch
BuildRequires:	texinfo
BuildRequires:	autoconf2.5
BuildRequires:	automake1.4

%description
The GNU time utility runs another program, collects information about
the resources used by that program while it is running and
displays the results.

Time can help developers optimize their programs.

The resources that `time' can report on fall into the general
categories of time, memory, I/O, and IPC calls.

The GNU version can format the output in arbitrary ways by using a 
printf-style format string to include various resource measurements.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0

export FORCE_AUTOCONF_2_5=1
aclocal-1.4
autoconf
automake-1.4 -a
#authoheader

%build

%configure2_5x
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_infodir}/%{name}.info*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7-37mdv2011.0
+ Revision: 670683
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-36mdv2011.0
+ Revision: 607995
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-35mdv2010.1
+ Revision: 520284
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.7-34mdv2010.0
+ Revision: 427369
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7-33mdv2009.1
+ Revision: 317693
- use %%optflags and %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.7-32mdv2009.0
+ Revision: 225717
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7-31mdv2008.1
+ Revision: 179649
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Feb 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7-30mdv2007.0
+ Revision: 120246
- fix typo

* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7-29mdv2007.1
+ Revision: 119978
- Import time

* Fri Oct 07 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.7-28mdk
- fix summary
- add prereq on info-install (#17417)

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.7-27mdk
- force use of autoconf2.5 and automake-1.4
- cosmetics
- wipe out buildroot before installing

* Tue Apr 20 2004 Michael Scherer <misc@mandrake.org> 1.7-26mdk 
- Birthday Rebuild
- some cosmetics
- Remove filebased requires, since basesystem already install everything

