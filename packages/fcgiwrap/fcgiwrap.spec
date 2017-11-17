%if 0%{?rhel} < 7
%bcond_with init_systemd
%bcond_without init_sysv
%else
%bcond_with init_sysv
%bcond_without init_systemd
%endif

Name:           fcgiwrap
Version:        1.1.0
Release:        2%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            http://nginx.localdomain.pl/wiki/FcgiWrap
Group:          System Environment/Daemons

Source0:        https://github.com/gnosek/fcgiwrap/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fcgi-devel
Requires:      spawn-fcgi

%{?with_init_systemd:BuildRequires: systemd-devel}
%if %{with init_systemd}
%{?systemd_requires: %systemd_requires}
%endif

%description
fcgiwrap is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other web servers
that may need it).


%prep
%setup -q


%build
sed 's#=http#=apache#g' -i systemd/fcgiwrap.service
autoreconf -i
%configure --prefix=""
make


%install
make install DESTDIR=%{buildroot}

%files
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*
%if %{with init_systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%endif

%changelog

* Fri Feb 08 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.1.0-1
- new upstream release.
* Fri Jan 11 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3.20120908-1
- Change version to increase monotonously.
* Wed Jan  9 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-3.gitb9f03e6377
- Make the rpm relocatable.
* Tue Dec 25 2012 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-2.gitb9f03e6377
* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
