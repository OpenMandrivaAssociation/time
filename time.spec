%global optflags %{optflags} -Oz

Summary:	A GNU utility for monitoring a program's use of system resources
Name:		time
Version:	1.10
Release:	1
License:	GPL
Group:		Monitoring
URL:		https://www.gnu.org/directory/GNU/time.html
Source0:	http://ftp.gnu.org/pub/gnu/time/%{name}-%{version}.tar.gz
BuildSystem:	autotools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool
BuildRequires:	make
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


%files
%doc NEWS README
%{_bindir}/%{name}
%doc %{_infodir}/%{name}.info*
