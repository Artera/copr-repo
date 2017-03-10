Summary: Nginx Anti XSS & SQL Injection (module for mainline nginx)
Name: nginx-mod-naxsi
Version: 0.55.3
Release: 1%{?dist}
Vendor: Artera
URL: https://github.com/nbs-system/naxsi

%define _modname            naxsi
%define _nginxver           1.10.2
%define nginx_config_dir    %{_sysconfdir}/nginx
%define nginx_build_dir     %{_builddir}/nginx-%{_nginxver}
%define mod_build_dir       %{_builddir}/%{_modname}-%{version}

Source0: http://nginx.org/download/nginx-%{_nginxver}.tar.gz
Source1: https://github.com/nbs-system/naxsi/archive/%{version}/%{_modname}-%{version}.tar.gz

Requires: nginx
BuildRequires: nginx
BuildRequires: expat-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: httpd-devel
BuildRequires: lua-devel
BuildRequires: yajl-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: zlib-devel
BuildRequires: pcre-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: gd-devel

License: GPL-v3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
NAXSI is an open-source, high performance, low rules maintenance WAF for NGINX.

%prep
%setup -q -n nginx-%{_nginxver}
%setup -T -D -b 1 -n %{_modname}-%{version}

%build
cd %{_builddir}/nginx-%{_nginxver}
./configure "$(nginx -V 2>&1 | grep 'configure arguments' | sed -r 's@^[^:]+: @@')" --add-dynamic-module=../%{_modname}-%{version}/naxsi_src
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{nginx_build_dir}/objs/ngx_http_naxsi_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_naxsi_module.so

%{__install} -Dm644 %{mod_build_dir}/naxsi_config/naxsi_core.rules \
    $RPM_BUILD_ROOT%{nginx_config_dir}/naxsi_core.rules

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{nginx_config_dir}/naxsi_core.rules
%{_libdir}/nginx/modules/*.so
