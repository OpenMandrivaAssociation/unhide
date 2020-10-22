Name:           unhide
Version:        20200120
Release:        1
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits
Group:          System/Configuration/Other
License:        GPLv3+
URL:            http://www.unhide-forensics.info/
#Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz
Sources:	https://github.com/YJesus/Unhide/releases/download/%{version}/unhide_%{version}.tgz
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
gcc %{optflags} %{ldflags} -pthread unhide-linux*.c unhide-output.c -o unhide-linux
gcc %{optflags} %{ldflags} unhide-tcp.c unhide-tcp-fast.c unhide-output.c -o unhide-tcp
gcc %{optflags} %{ldflags} unhide_rb.c -o unhide_rb
gcc %{optflags} %{ldflags} unhide-gids.c unhide-output.c -o unhide-gids
%install

# binaries
install -Dp -m0755 unhide-linux %{buildroot}%{_sbindir}/unhide-linux
install -Dp -m0755 unhide-tcp %{buildroot}%{_sbindir}/unhide-tcp
install -Dp -m0755 unhide_rb %{buildroot}%{_sbindir}/unhide_rb
install -Dp -m0755 unhide-gids %{buildroot}%{_sbindir}/unhide-gids

# man pages
install -d %{buildroot}%{_mandir}/man8

install -p -m0644 man/*.8 -t %{buildroot}%{_mandir}/man8/

# symlinks
ln -s unhide-linux %{buildroot}%{_sbindir}/unhide
ln -s unhide.8 %{buildroot}%{_mandir}/man8/unhide-linux.8

%files
%license COPYING
%doc README.txt TODO
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


