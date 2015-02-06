Name:           unhide
Version:        20110113
Release:        2
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits
Group:          System/Configuration/Other
License:        GPLv3+
URL:            http://www.unhide-forensics.info/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Unhide is a forensic tool to find hidden processes and TCP/UDP ports by
rootkits / LKMs or by another hidden technique. It includes two
utilities: unhide and unhide-tcp.

Unhide detects hidden processes using six techniques:

  - Compare /proc vs /bin/ps output
  - Compare info gathered from /bin/ps with info gathered by walking through
    the procfs.
  - Compare info gathered from /bin/ps with info gathered from syscalls
    (syscall scanning).
  - Full PIDs space occupation (PIDs bruteforcing)
  - Reverse search, verify that all thread seen by ps are also seen by
    the kernel ( /bin/ps output vs /proc, procfs walking and syscall )
  - Quick compare /proc, procfs walking and syscall vs /bin/ps output.

Unhide-tcp identifies TCP/UDP ports that are listening but are not listed
in /bin/netstat through brute forcing of all TCP/UDP ports available.

%prep
%setup -q -n %{name}-%{version}

%build
gcc %{optflags} %{ldflags} -pthread unhide-linux26.c -o unhide-linux26
gcc %{optflags} %{ldflags} unhide-tcp.c -o unhide-tcp


%install
rm -rf %{buildroot}
install -Dp -m0755 unhide-linux26 %{buildroot}%{_sbindir}/unhide-linux26
install -Dp -m0755 unhide-tcp %{buildroot}%{_sbindir}/unhide-tcp
install -Dp -m0644 man/unhide.8 %{buildroot}%{_mandir}/man8/unhide.8
install -Dp -m0644 man/unhide-tcp.8 %{buildroot}%{_mandir}/man8/unhide-tcp.8

pushd %{buildroot}%{_sbindir}
	ln -s unhide-linux26 unhide
popd

pushd %{buildroot}%{_mandir}/man8
        ln -s unhide.8 unhide-linux26.8
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc changelog LEEME.txt README.txt
%{_mandir}/man8/unhide*
%{_sbindir}/unhide*


%changelog
* Tue Feb 08 2011 Jani Välimaa <wally@mandriva.org> 20110113-1mdv2011.0
+ Revision: 636928
- new version 20110113
- fix url and source tags

* Sun Nov 14 2010 Jani Välimaa <wally@mandriva.org> 20100819-2mdv2011.0
+ Revision: 597542
- build with LDFLAGS
- add symlink for man page too

* Sat Sep 25 2010 Jani Välimaa <wally@mandriva.org> 20100819-1mdv2011.0
+ Revision: 580960
- new version 20100819
- fix license and description

* Mon Aug 02 2010 Jani Välimaa <wally@mandriva.org> 20100201-1mdv2011.0
+ Revision: 565116
- fix source tag
- import unhide


