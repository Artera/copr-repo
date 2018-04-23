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
Source0:    %{name}-%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: cmake

%{?with_init_systemd:BuildRequires: systemd-devel}
%if %{with init_systemd}
%{?systemd_requires: %systemd_requires}
%endif

%description
%{summary}

%prep
%setup -c %{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}
cargo build --release

%install
cargo install --root %{buildroot}/usr
rm -f %{buildroot}/usr/.crates.toml

%{__install} -Dm644 %{_builddir}/%{name}-%{version}/%{name}.service \
    $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%{__install} -Dm644 %{_builddir}/%{name}-%{version}/filebeat-mysqlslow.yml \
    $RPM_BUILD_ROOT%{_sysconfdir}/filebeat/filebeat-mysqlslow.yml

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
