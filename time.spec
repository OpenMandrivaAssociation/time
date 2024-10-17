%global optflags %{optflags} -Oz

Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.9
Release:	7
License:	GPL
Group:		Monitoring
URL:		https://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.gz
# Fix measuring time when a clock experiences a jump, bug #1004416,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2013-09/msg00003.html>
Patch0:		time-1.8-Prefer-clock_gettime-CLOCK_MONOTONIC.patch
Patch1:		time-1.9-clang-16.patch
Patch2:		time-1.9-Close-outfp-before-exec.patch
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
%autosetup -p1
autoreconf -fiv
%configure

%build
%make_build

%install
%make_install

%files
%doc NEWS README
%{_bindir}/%{name}
%doc %{_infodir}/%{name}.info*
