Summary: Directives "echo", "sleep", "time" and more
Name: nginx-mod-echo
Version: 0.60
Release: 1%{?dist}
Vendor: Artera
URL: https://github.com/openresty/echo-nginx-module

%define _modname            echo
%define _nginxver           1.10.2
%define nginx_config_dir    %{_sysconfdir}/nginx
%define nginx_build_dir     %{_builddir}/nginx-%{_nginxver}

Source0: http://nginx.org/download/nginx-%{_nginxver}.tar.gz
Source1: https://github.com/openresty/echo-nginx-module/archive/v%{version}/%{_modname}-%{version}.tar.gz

Patch0: https://patch-diff.githubusercontent.com/raw/openresty/echo-nginx-module/pull/65.patch

Requires: nginx
BuildRequires: nginx
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: perl-devel
BuildRequires: gd-devel
BuildRequires: GeoIP-devel
BuildRequires: libxslt-devel
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: gperftools-devel

License: BSD

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Directives "echo", "sleep", "time" and more.

%prep
%setup -q -n nginx-%{_nginxver}
%setup -T -D -b 1 -n %{_modname}-nginx-module-%{version}
%patch0 -p1

%build
cd %{_builddir}/nginx-%{_nginxver}
./configure %(nginx -V 2>&1 | grep 'configure arguments' | sed -r 's@^[^:]+: @@') --add-dynamic-module=../%{_modname}-nginx-module-%{version}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{nginx_build_dir}/objs/ngx_http_echo_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_echo_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
