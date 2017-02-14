#
%define nginx_home %{_localstatedir}/cache/nginx
%define nginx_user nginx
%define nginx_group nginx
%define nginx_loggroup adm

# distribution specific definitions
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (0%{?suse_version} == 1315)

%if 0%{?rhel}  == 5
%define _group System Environment/Daemons
Requires(pre): shadow-utils
Requires: initscripts >= 8.36
Requires(post): chkconfig
Requires: openssl
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: GeoIP-devel
%endif

%if 0%{?rhel}  == 6
%define _group System Environment/Daemons
%define with_http2 1
Requires(pre): shadow-utils
Requires: initscripts >= 8.36
Requires(post): chkconfig
Requires: openssl >= 1.0.1
BuildRequires: openssl-devel >= 1.0.1
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Embed
BuildRequires: GeoIP-devel
%endif

%if 0%{?rhel}  == 7
Group: System Environment/Daemons
%define epoch 1
%define with_http2 1
Epoch: %{epoch}
Requires(pre): shadow-utils
Requires: systemd
Requires: openssl >= 1.0.1
BuildRequires: systemd
BuildRequires: openssl-devel >= 1.0.1
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Embed
BuildRequires: GeoIP-devel
%endif

%if 0%{?suse_version} == 1315
%define _group Productivity/Networking/Web/Servers
%define with_http2 1
%define nginx_loggroup trusted
Requires(pre): shadow
Requires: systemd
BuildRequires: libopenssl-devel
BuildRequires: systemd
BuildRequires: perl
BuildRequires: libGeoIP-devel
%endif

# end of distribution specific definitions

Requires: lua
Requires: yajl
Requires: curl
Requires: libxml2
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

Provides: webserver
Provides: nginx = %{version}
Conflicts: nginx

Summary: High performance web server
Name: nginx-pro
Version: 1.11.8
Release: 1%{?dist}.ngx
Vendor: nginx inc.
URL: http://nginx.org/

%define _davextver     0.0.3
%define _pushstreamver 0.5.2
%define _cachepurgever 2.3.1
%define _modsecver     2.9.1
%define _devkitver     0.3.0
%define _redisver      0.3.8
%define _pagespeedver  latest-stable
%define _psolver       1.11.33.4
%define _njsver        0.1.7

%define _ngxbrotliver  bfd2885b2da4d763fed18f49216bb935223cd34b
%define _brotliver     222564a95d9ab58865a096b8d9f7324ea5f2e03e

# openresty
%define _echo_ver         0.60
%define _lua_ver          0.10.7
%define _srcache_ver      0.31
%define _set_misc_ver     0.31
%define _redis2_ver       0.13
%define _memc_ver         0.17
%define _headers_more_ver 0.32

Source0: http://nginx.org/download/nginx-%{version}.tar.gz
Source1: nginx.logrotate
Source2: nginx.init.in
Source3: nginx.sysconf
Source4: nginx.conf
Source5: nginx.vh.default.conf
Source7: nginx.upgrade.sh
Source8: nginx.service
Source9: modsec-recommended.conf
Source10: https://github.com/SpiderLabs/ModSecurity/archive/v%{_modsecver}/modsecurity-%{_modsecver}.tar.gz
Source11: https://github.com/simpl/ngx_devel_kit/archive/v%{_devkitver}/ngx_devel_kit-%{_devkitver}.tar.gz
Source12: https://github.com/arut/nginx-dav-ext-module/archive/v%{_davextver}/nginx-dav-ext-module-%{_davextver}.tar.gz
Source13: https://github.com/mtorromeo/ngx_cache_purge/archive/%{_cachepurgever}/nginx_cache_purge-%{_cachepurgever}.tar.gz
Source14: https://github.com/wandenberg/nginx-push-stream-module/archive/%{_pushstreamver}/nginx-push-stream-module-%{_pushstreamver}.tar.gz
Source15: http://people.freebsd.org/~osa/ngx_http_redis-%{_redisver}.tar.gz
Source16: https://github.com/openresty/echo-nginx-module/archive/v%{_echo_ver}/echo-nginx-module-%{_echo_ver}.tar.gz
Source17: https://github.com/openresty/lua-nginx-module/archive/v%{_lua_ver}/lua-nginx-module-%{_lua_ver}.tar.gz
Source18: https://github.com/openresty/srcache-nginx-module/archive/v%{_srcache_ver}/srcache-nginx-module-%{_srcache_ver}.tar.gz
Source19: https://github.com/openresty/set-misc-nginx-module/archive/v%{_set_misc_ver}/set-misc-nginx-module-%{_set_misc_ver}.tar.gz
Source20: https://github.com/openresty/redis2-nginx-module/archive/v%{_redis2_ver}/redis2-nginx-module-%{_redis2_ver}.tar.gz
Source21: https://github.com/openresty/memc-nginx-module/archive/v%{_memc_ver}/memc-nginx-module-%{_memc_ver}.tar.gz
Source22: https://github.com/openresty/headers-more-nginx-module/archive/v%{_headers_more_ver}/headers-more-nginx-module-%{_headers_more_ver}.tar.gz
Source23: https://github.com/pagespeed/ngx_pagespeed/archive/latest-stable/pagespeed-module-%{_pagespeedver}.tar.gz
Source24: https://dl.google.com/dl/page-speed/psol/%{_psolver}.tar.gz
Source25: http://hg.nginx.org/njs/archive/%{_njsver}.tar.gz
Source26: nginx-debug.service
Source27: https://github.com/google/ngx_brotli/archive/%{_ngxbrotliver}/ngx_brotli-%{_ngxbrotliver}.tar.gz
Source28: https://github.com/google/brotli/archive/%{_brotliver}/brotli-%{_brotliver}.tar.gz

Source50: https://github.com/openresty/redis2-nginx-module/commit/8cc7304787ae9542db4feb50d9e27beb485caa0f.patch
Source51: https://github.com/openresty/memc-nginx-module/commit/c08cb7043440e427867838caf21cfd1e6cb2127a.patch

License: 2-clause BSD-like license

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%define bdir %{_builddir}/nginx-%{version}

%description
nginx [engine x] is an HTTP and reverse proxy server, as well as
a mail proxy server.

%prep
%setup -q -n nginx-%{version}
%setup -T -D -b 10 -n nginx-%{version}
%setup -T -D -b 11 -n nginx-%{version}
%setup -T -D -b 12 -n nginx-%{version}
%setup -T -D -b 13 -n nginx-%{version}
%setup -T -D -b 14 -n nginx-%{version}
%setup -T -D -b 15 -n nginx-%{version}
%setup -T -D -b 16 -n nginx-%{version}
%setup -T -D -b 17 -n nginx-%{version}
%setup -T -D -b 18 -n nginx-%{version}
%setup -T -D -b 19 -n nginx-%{version}
%setup -T -D -b 20 -n nginx-%{version}
%setup -T -D -b 21 -n nginx-%{version}
%setup -T -D -b 22 -n nginx-%{version}
%setup -T -D -b 23 -n nginx-%{version}
%setup -T -D -b 24 -n nginx-%{version}
%setup -T -D -b 25 -n nginx-%{version}
%setup -T -D -b 27 -n nginx-%{version}
%setup -T -D -b 28 -n nginx-%{version}
sed -e 's|%%DEFAULTSTART%%|2 3 4 5|g' -e 's|%%DEFAULTSTOP%%|0 1 6|g' \
    -e 's|%%PROVIDES%%|nginx|g' < %{SOURCE2} > nginx.init
sed -e 's|%%DEFAULTSTART%%||g' -e 's|%%DEFAULTSTOP%%|0 1 2 3 4 5 6|g' \
    -e 's|%%PROVIDES%%|nginx-debug|g' < %{SOURCE2} > nginx-debug.init

%build

cd %{_builddir}/redis2-nginx-module-0.13
patch -p1 -i %{SOURCE50}

cd %{_builddir}/memc-nginx-module-0.17
patch -p1 -i %{SOURCE51}

cd %{_builddir}/ngx_brotli-%{_ngxbrotliver}/deps
rm -rf brotli
ln -s ../../brotli-%{_brotliver} brotli

cd %{_builddir}/ngx_pagespeed-%{_pagespeedver}
ln -s ../psol

cd %{_builddir}/ModSecurity-%{_modsecver}
sh autogen.sh
CFLAGS="-g -O0" ./configure \
        --prefix=%{_prefix} \
        --with-apr=%{_bindir}/apr-1-config \
        --enable-standalone-module \
        --disable-apache2-module \
        --enable-pcre-study \
        --enable-pcre-jit \
        --enable-pcre-match-limit=1000 \
        --enable-pcre-match-limit-recursion=1000 \
        --enable-lua-cache
sed -r '/\$\$base/d' -i standalone/Makefile
make
make DESTDIR=%{_builddir}/ModSecurity-%{_modsecver}/install install

COMMON_CONFIGURE_ARGS=(
        --prefix=%{_sysconfdir}/nginx
        --sbin-path=%{_sbindir}/nginx
        --modules-path=%{_libdir}/nginx/modules
        --conf-path=%{_sysconfdir}/nginx/nginx.conf
        --error-log-path=%{_localstatedir}/log/nginx/error.log
        --http-log-path=%{_localstatedir}/log/nginx/access.log
        --pid-path=%{_localstatedir}/run/nginx.pid
        --lock-path=%{_localstatedir}/run/nginx.lock
        --http-client-body-temp-path=%{_localstatedir}/cache/nginx/client_temp
        --http-proxy-temp-path=%{_localstatedir}/cache/nginx/proxy_temp
        --http-fastcgi-temp-path=%{_localstatedir}/cache/nginx/fastcgi_temp
        --http-uwsgi-temp-path=%{_localstatedir}/cache/nginx/uwsgi_temp
        --http-scgi-temp-path=%{_localstatedir}/cache/nginx/scgi_temp
        --user=%{nginx_user}
        --group=%{nginx_group}
        %{?with_http2:--with-http_v2_module}
        --with-http_ssl_module
        --with-http_realip_module
        --with-http_addition_module
        --with-http_sub_module
        --with-http_dav_module
        --with-http_geoip_module=dynamic
        --with-http_flv_module
        --with-http_mp4_module
        --with-http_gunzip_module
        --with-http_gzip_static_module
        --with-http_random_index_module
        --with-http_secure_link_module
        --with-http_stub_status_module
        --with-http_auth_request_module
        --with-http_xslt_module=dynamic
        --with-http_image_filter_module=dynamic
        --with-stream=dynamic
        --with-stream_ssl_module
        --with-stream_realip_module
        --with-stream_ssl_preread_module
        --with-stream_geoip_module=dynamic
        --with-http_perl_module=dynamic
        --with-mail=dynamic
        --with-mail_ssl_module
        --with-file-aio
        --with-threads
        --with-http_auth_request_module
        --add-dynamic-module=../ngx_devel_kit-%{_devkitver}
        --add-dynamic-module=../ngx_cache_purge-%{_cachepurgever}
        --add-module=../nginx-dav-ext-module-%{_davextver}
        --add-dynamic-module=../nginx-push-stream-module-%{_pushstreamver}
        --add-module=../ModSecurity-%{_modsecver}/nginx/modsecurity
        --add-dynamic-module=../ngx_http_redis-%{_redisver}
        --add-dynamic-module=../ngx_pagespeed-%{_pagespeedver}
        --add-dynamic-module=../njs-%{_njsver}/nginx
        --add-dynamic-module=../echo-nginx-module-%{_echo_ver}
        --add-dynamic-module=../lua-nginx-module-%{_lua_ver}
        --add-dynamic-module=../srcache-nginx-module-%{_srcache_ver}
        --add-dynamic-module=../set-misc-nginx-module-%{_set_misc_ver}
        --add-dynamic-module=../redis2-nginx-module-%{_redis2_ver}
        --add-dynamic-module=../memc-nginx-module-%{_memc_ver}
        --add-dynamic-module=../headers-more-nginx-module-%{_headers_more_ver}
        --add-dynamic-module=../ngx_brotli-%{_ngxbrotliver}
        --with-ld-opt="$RPM_LD_FLAGS -Wl,-E"
        --with-cc-opt="%{optflags} $(pcre-config --cflags)"
)

export NGX_BROTLI_STATIC_MODULE_ONLY=1

cd %{bdir}
./configure "${COMMON_CONFIGURE_ARGS[@]}" --with-debug
make %{?_smp_mflags}
%{__mv} %{bdir}/objs/nginx \
    %{bdir}/objs/nginx-debug
%{__mv} %{bdir}/objs/ngx_http_xslt_filter_module.so \
    %{bdir}/objs/ngx_http_xslt_filter_module-debug.so
%{__mv} %{bdir}/objs/ngx_http_image_filter_module.so \
    %{bdir}/objs/ngx_http_image_filter_module-debug.so
%{__mv} %{bdir}/objs/ngx_http_geoip_module.so \
    %{bdir}/objs/ngx_http_geoip_module-debug.so
%{__mv} %{bdir}/objs/ngx_http_perl_module.so \
    %{bdir}/objs/ngx_http_perl_module-debug.so
%{__mv} %{bdir}/objs/src/http/modules/perl/blib/arch/auto/nginx/nginx.so \
    %{bdir}/objs/src/http/modules/perl/blib/arch/auto/nginx/nginx-debug.so
%{__mv} %{bdir}/objs/ngx_http_js_module.so \
    %{bdir}/objs/ngx_http_js_module-debug.so
%{__mv} %{bdir}/objs/ngx_stream_js_module.so \
    %{bdir}/objs/ngx_stream_js_module-debug.so
%{__mv} %{bdir}/objs/ngx_stream_geoip_module.so \
    %{bdir}/objs/ngx_stream_geoip_module-debug.so
./configure "${COMMON_CONFIGURE_ARGS[@]}"
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLDIRS=vendor

find %{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f '{}' \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f '{}' \;
find %{buildroot} -type f -empty -exec rm -f '{}' \;
find %{buildroot} -type f -iname '*.so' -exec chmod 0755 '{}' \;

%{__mkdir} -p %{buildroot}%{_datadir}/nginx
%{__mv} %{buildroot}%{_sysconfdir}/nginx/html %{buildroot}%{_datadir}/nginx/

%{__rm} -f %{buildroot}%{_sysconfdir}/nginx/*.default
%{__rm} -f %{buildroot}%{_sysconfdir}/nginx/fastcgi.conf

%{__mkdir} -p %{buildroot}%{_localstatedir}/log/nginx
%{__mkdir} -p %{buildroot}%{_localstatedir}/run/nginx
%{__mkdir} -p %{buildroot}%{_localstatedir}/cache/nginx

%{__mkdir} -p $RPM_BUILD_ROOT%{_libdir}/nginx/modules
cd $RPM_BUILD_ROOT%{_sysconfdir}/nginx && \
    %{__ln_s} ../..%{_libdir}/nginx/modules modules && cd -

%{__mkdir} -p %{buildroot}%{_sysconfdir}/nginx/conf.d
%{__rm} %{buildroot}%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE4} \
   %{buildroot}%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE5} \
   %{buildroot}%{_sysconfdir}/nginx/conf.d/default.conf

%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 644 -p %{SOURCE3} \
   %{buildroot}%{_sysconfdir}/sysconfig/nginx
%{__install} -m 644 -p %{SOURCE25} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nginx-debug

%if %{use_systemd}
# install systemd-specific files
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %SOURCE8 \
        %{buildroot}%{_unitdir}/nginx.service
%{__install} -m644 %SOURCE26 \
    $RPM_BUILD_ROOT%{_unitdir}/nginx-debug.service
%{__mkdir} -p %{buildroot}%{_libexecdir}/initscripts/legacy-actions/nginx
%{__install} -m755 %SOURCE7 \
        %{buildroot}%{_libexecdir}/initscripts/legacy-actions/nginx/upgrade
%else
# install SYSV init stuff
%{__mkdir} -p %{buildroot}%{_initrddir}
%{__install} -m755 %{SOURCE2} \
   %{buildroot}%{_initrddir}/nginx
%endif

# install log rotation stuff
%{__mkdir} -p %{buildroot}%{_sysconfdir}/logrotate.d
%{__install} -m 644 -p %{SOURCE1} \
   %{buildroot}%{_sysconfdir}/logrotate.d/nginx

%{__install} -m755 %{bdir}/objs/nginx-debug \
    $RPM_BUILD_ROOT%{_sbindir}/nginx-debug

%{__install} -m644 %{bdir}/objs/ngx_http_xslt_filter_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_xslt_filter_module-debug.so
%{__install} -m644 %{bdir}/objs/ngx_http_image_filter_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_image_filter_module-debug.so
%{__install} -m644 %{bdir}/objs/ngx_http_geoip_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_geoip_module-debug.so
%{__install} -m644 %{bdir}/objs/ngx_http_perl_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_perl_module-debug.so
%{__mkdir} -p $RPM_BUILD_ROOT%{perl_vendorarch}/auto/nginx
%{__install} -m644 %{bdir}/objs/src/http/modules/perl/blib/arch/auto/nginx/nginx-debug.so \
    $RPM_BUILD_ROOT%{perl_vendorarch}/auto/nginx/nginx-debug.so
%{__install} -m644 %{bdir}/objs/ngx_http_js_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_js_module-debug.so
%{__install} -m644 %{bdir}/objs/ngx_stream_js_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_stream_js_module-debug.so
%{__install} -m644 %{bdir}/objs/ngx_stream_geoip_module-debug.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_stream_geoip_module-debug.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)

%{_sbindir}/nginx
%{_sbindir}/nginx-debug

%{_mandir}/man*/nginx*

%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%{_sysconfdir}/nginx/modules

%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/default.conf
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/fastcgi_params
%config(noreplace) %{_sysconfdir}/nginx/scgi_params
%config(noreplace) %{_sysconfdir}/nginx/uwsgi_params
%config(noreplace) %{_sysconfdir}/nginx/koi-utf
%config(noreplace) %{_sysconfdir}/nginx/koi-win
%config(noreplace) %{_sysconfdir}/nginx/win-utf

%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%config(noreplace) %{_sysconfdir}/sysconfig/nginx
%config(noreplace) %{_sysconfdir}/sysconfig/nginx-debug
%if %{use_systemd}
%{_unitdir}/nginx.service
%{_unitdir}/nginx-debug.service
%dir %{_libexecdir}/initscripts/legacy-actions/nginx
%{_libexecdir}/initscripts/legacy-actions/nginx/*
%else
%{_initrddir}/nginx
%{_initrddir}/nginx-debug
%endif

%dir %{perl_vendorarch}/auto/nginx
%{perl_vendorarch}/nginx.pm
%{perl_vendorarch}/auto/nginx/nginx.so
%{perl_vendorarch}/auto/nginx/nginx-debug.so

%dir %{_datadir}/nginx
%dir %{_datadir}/nginx/html
%{_datadir}/nginx/html/*
%{_libdir}/nginx/modules/*.so

%attr(0755,root,root) %dir %{_localstatedir}/cache/nginx
%attr(0755,root,root) %dir %{_localstatedir}/log/nginx

%pre
# Add the "nginx" user
getent group %{nginx_group} >/dev/null || groupadd -r %{nginx_group}
getent passwd %{nginx_user} >/dev/null || \
    useradd -r -g %{nginx_group} -s /sbin/nologin \
    -d %{nginx_home} -c "nginx user"  %{nginx_user}
exit 0

%post
# Register the nginx service
if [ $1 -eq 1 ]; then
%if %{use_systemd}
    /usr/bin/systemctl preset nginx.service >/dev/null 2>&1 ||:
%else
    /sbin/chkconfig --add nginx
    /sbin/chkconfig --add nginx-debug
%endif

    # Touch and set permisions on default log files on installation

    if [ -d %{_localstatedir}/log/nginx ]; then
        if [ ! -e %{_localstatedir}/log/nginx/access.log ]; then
            touch %{_localstatedir}/log/nginx/access.log
            %{__chmod} 640 %{_localstatedir}/log/nginx/access.log
            %{__chown} nginx:%{nginx_loggroup} %{_localstatedir}/log/nginx/access.log
        fi

        if [ ! -e %{_localstatedir}/log/nginx/error.log ]; then
            touch %{_localstatedir}/log/nginx/error.log
            %{__chmod} 640 %{_localstatedir}/log/nginx/error.log
            %{__chown} nginx:%{nginx_loggroup} %{_localstatedir}/log/nginx/error.log
        fi
    fi
fi

%preun
if [ $1 -eq 0 ]; then
%if %use_systemd
    /usr/bin/systemctl --no-reload disable nginx nginx-debug >/dev/null 2>&1 ||:
    /usr/bin/systemctl stop nginx nginx-debug >/dev/null 2>&1 ||:
%else
    /sbin/service nginx stop > /dev/null 2>&1
    /sbin/chkconfig --del nginx
    /sbin/chkconfig --del nginx-debug
%endif
fi

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:
%endif
if [ $1 -ge 1 ]; then
    /sbin/service nginx status  >/dev/null 2>&1 || exit 0
    /sbin/service nginx upgrade >/dev/null 2>&1 || echo \
        "Binary upgrade failed, please check nginx's error.log"
fi
