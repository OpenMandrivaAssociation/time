Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.7
Release:	38
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
rm -rf %{buildroot}
%makeinstall_std

%files
%doc NEWS README
%{_bindir}/%{name}
%{_infodir}/%{name}.info*

