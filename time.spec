Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.8
Release:	1
License:	GPL
Group:		Monitoring
URL:		http://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.gz
# Do not print command failure in POSIX mode, in upstream after 1.8
# <https://lists.gnu.org/archive/html/bug-time/2017-11/msg00001.html>
Patch0:		time-1.8-time-remove-Command-exited-with-non-zero-status-in-P.patch
# Silent compiler warnings, in upstream after 1.8
Patch1:		time-1.8-time-use-noreturn-to-pacify-gcc-7.patch
# Correct test added in
# time-remove-Command-exited-with-non-zero-status-in-P.patch
Patch2:		time-1.8-Accept-numeric-values-in-tests-time-posix-quiet.sh.patch
# Bug #527276
Patch3:		time-1.8-Recompute-CPU-usage-at-microsecond-level.patch
# Fix measuring time when a clock experiences a jump, bug #1004416,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2013-09/msg00003.html>
Patch4:		time-1.8-Prefer-clock_gettime-CLOCK_MONOTONIC.patch
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
chmod +x tests/time-posix-quiet.sh
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

autoreconf -fiv

%build
%configure
%make

%install
%makeinstall

%files
%doc NEWS README
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
