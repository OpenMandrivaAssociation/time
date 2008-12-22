Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.7
Release:	%mkrel 33
License:	GPL
Group:		Monitoring
URL:		http://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.bz2
Patch0:		time-1.7.info.patch
Patch1:		time-1.7-ressource.patch
Patch2:		time-1.7-quiet.1.patch
Patch3:		time-1.7-fixinfo.patch
Patch4:		time-1.7-build.patch
BuildRequires:	texinfo autoconf2.5 automake1.4
Requires(pre):	info-install
Requires(preun): info-install
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%_install_info %name.info

%preun
%_remove_install_info %name.info

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_infodir}/%{name}.info*


