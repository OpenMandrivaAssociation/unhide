Name:           unhide
Version:        20100201
Release:        %mkrel 1
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits
Group:          System/Configuration/Other
License:        GPLv3
URL:            http://www.security-projects.com/?Unhide
Source0:        http://www.security-projects.com/unhide-20100201.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Unhide is a forensic tool to find processes and TCP/UDP ports hidden by
rootkits, Linux kernel modules or by other techniques. It includes two
utilities: unhide and unhide-tcp.

Unhide detects hidden processes using three techniques:

 - comparing the output of /proc and /bin/ps
 - comparing the information gathered from /bin/ps with the one gathered
   from system calls (syscall scanning)
 - full scan of the process ID space (PIDs bruteforcing)

unhide-tcp identifies TCP/UDP ports that are listening but are not listed
in /bin/netstat through brute forcing of all TCP/UDP ports available.

%prep
%setup -q -n %{name}-%{version}

%build
gcc %{optflags} -lpthread unhide-linux26.c -o unhide-linux26
gcc %{optflags} unhide-tcp.c -o unhide-tcp


%install
rm -rf %{buildroot}
install -Dp -m0755 unhide-linux26 %{buildroot}%{_sbindir}/unhide-linux26
install -Dp -m0755 unhide-tcp %{buildroot}%{_sbindir}/unhide-tcp
install -Dp -m0644 man/unhide.8 %{buildroot}%{_mandir}/man8/unhide.8
install -Dp -m0644 man/unhide-tcp.8 %{buildroot}%{_mandir}/man8/unhide-tcp.8

pushd %{buildroot}%{_sbindir}
	ln -s unhide-linux26 unhide
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING LEEME.txt README.txt
%{_mandir}/man8/unhide*
%{_sbindir}/unhide*
