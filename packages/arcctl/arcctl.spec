%define debug_package %{nil}

Name:       arcctl
Version:    1.14.7_150519
Release:    1%{?dist}
Summary:    CLI tools to manage Areca's ARC11xx/ARC12xx/ARC16xx/ARC18xx RAID controllers

Group:      System Environment/Daemons
License:    custom
URL:        http://www.areca.com.tw/support/s_linux/linux.htm
Source0:    http://www.areca.us/support/s_linux/cli/linuxcli_V%{version}.zip

%description
CLI tools to manage Areca's ARC11xx/ARC12xx/ARC16xx/ARC18xx RAID controllers.

%prep
%setup -q -n "linuxcli_V%{version}"

%build
# there's nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dm 0755 x86_64/cli64 %{buildroot}/%{_bindir}/arcctl

%files
%{_bindir}/arcctl

%changelog
* Mon Apr 18 2016 Massimiliano Torromeo <massimiliano.torromeo@gmail.com> - 1.14.7-1
- Initial packaging for CentOS.
