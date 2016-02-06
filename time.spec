Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.7
Release:	50
License:	GPL
Group:		Monitoring
URL:		http://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.bz2
Patch0:		time-1.7.info.patch
Patch1:		time-1.7-ressource.patch
Patch2:		time-1.7-quiet.1.patch
Patch3:		time-1.7-fixinfo.patch
Patch4:		time-1.7-build.patch
Patch5:		time-1.7-configure.patch
Patch6:		time-1.7-ru_maxrss-is-in-kilobytes-on-Linux.patch
Patch7:		time-1.7-Recompute-CPU-usage-at-microsecond-level.patch
BuildRequires:	texinfo

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
%patch5 -p1
%patch6 -p1
%patch7 -p1

autoreconf -fiv

%build
%configure
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall

%files
%doc NEWS README
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
