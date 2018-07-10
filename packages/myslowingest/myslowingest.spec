%if 0%{?rhel} < 7
%bcond_with init_systemd
%bcond_without init_sysv
%else
%bcond_with init_sysv
%bcond_without init_systemd
%endif

Name:       myslowingest
Version:    0.1.0
Release:    1%{?dist}
Summary:    Parses slowlog messages passed through standard input by a filebeat process and inserts the structured records into a sqlite database
License:    Proprietary

Group:      Applications/System
URL:        https://git.artera.it/sysadmin/myslowingest
ExclusiveArch: x86_64
Source0:    https://downloads.artera.it/%{name}-linux-bin-%{version}.gz
Source1:    myslowingest.service
Source2:    filebeat-mysqlslow.yml

%{?with_init_systemd:BuildRequires: systemd-devel}
%if %{with init_systemd}
%{?systemd_requires: %systemd_requires}
%endif

%description
%{summary}

%prep
gzip -dc %{SOURCE0} > %{_builddir}/%{name}

%install
%{__install} -Dm755 %{_builddir}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%{__install} -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/filebeat/filebeat-mysqlslow.yml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sysconfdir}/filebeat/filebeat-mysqlslow.yml
%if %{with init_systemd}
%{_unitdir}/%{name}.service
%endif

%changelog
* Mon Apr 23 2018 Massimiliano Torromeo <massimiliano.torromeo@artera.net> - 0.1.0
- First build