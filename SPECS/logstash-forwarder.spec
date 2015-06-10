%define debug_package %{nil}
%define __prefix /usr
#%define __commit a718299722376cf84b4ebd652586eada2af0e2f3

%if 0%{?rhel} < 7
%bcond_with init_systemd
%bcond_without init_sysv
%else
%bcond_with init_sysv
%bcond_without init_systemd
%endif

Name:           logstash-forwarder
Summary:        Logstash shipping tool using the lumberjack protocol
Version:        0.4.0
Release:        4.20150223gita718299%{?dist}
License:        Apache Software License 2.0
Group:          System Environment/Daemons
Prefix:         %{_prefix}

Url:            https://github.com/elasticsearch/logstash-forwarder
#Source0:        https://github.com/elasticsearch/logstash-forwarder/archive/%{__commit}/%{name}-%{version}-%{__commit}.tar.gz
Source0:        https://github.com/elasticsearch/logstash-forwarder/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        logstash-forwarder-init.d
Source2:        logstash-forwarder-sysconfig
Source3:        logstash-forwarder-config.conf
Source4:        logstash-forwarder.service
Source5:        logstash-forwarder-journal.service
Source6:        logstash-forwarder-journalctl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  golang
%{?with_init_systemd:BuildRequires: systemd}
%if %{with init_systemd}
%{?systemd_requires: %systemd_requires}
%endif


%description
A tool to collect logs locally in preparation for processing elsewhere.


%prep
#%setup -q -n %{name}-%{__commit}
%setup -q -n %{name}-%{version}


%build
go build


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{__prefix}/bin
#%{__install} -p -m 755  %{_builddir}/%{name}-%{__commit}/%{name}-%{__commit}
%{__install} -p -m 755  %{_builddir}/%{name}-%{version}/%{name}-%{version} %{buildroot}%{__prefix}/bin/logstash-forwarder

# Config
%{__install} -Dm644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logstash-forwarder.conf

# Misc
%{__mkdir} -p %{buildroot}%{_localstatedir}/run

# systemd
%if %{with init_systemd}
%{__install} -Dm644 %{SOURCE4} %{buildroot}%{_unitdir}/logstash-forwarder.service
%{__install} -Dm644 %{SOURCE5} %{buildroot}%{_unitdir}/logstash-forwarder-journal.service
%{__install} -Dm0755 %{SOURCE6} %{buildroot}/usr/lib/systemd/scripts/logstash-forwarder-journalctl
%else
%{__install} -Dm755 %{SOURCE1} %{buildroot}%{_initddir}/%{name}
%{__install} -Dm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%endif

# Create Home directory
%{__mkdir} -p %{buildroot}%{_sharedstatedir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
%if %{with init_systemd}
/usr/bin/systemctl daemon-reload
%else
/sbin/chkconfig --add %{name}
%endif


%preun
%if %{with init_systemd}
%systemd_preun %{name}.service
%systemd_preun %{name}-journal.service
%else
/sbin/service %{name} stop >/dev/null 2>&1
/sbin/chkconfig --del %{name}
%endif


%postun
%if %{with init_systemd}
%systemd_postun
%endif


%files
%defattr(-,root,root,-)
%{__prefix}/bin/logstash-forwarder

# Config
%config(noreplace) %{_sysconfdir}/logstash-forwarder.conf

# systemd
%if %{with init_systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-journal.service
/usr/lib/systemd/scripts/logstash-forwarder-journalctl
%else
%{_initddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif

%defattr(-,mail,mail,-)

# Home directory
%dir %{_sharedstatedir}/%{name}/
