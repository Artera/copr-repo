%if 0%{?rhel} < 7
%bcond_with init_systemd
%bcond_without init_sysv
%else
%bcond_with init_sysv
%bcond_without init_systemd
%endif

Name:           piler
Version:        1.1.1
Release:        1%{?dist}
Summary:        Open source email archiving solution with all the necessary features for your enterprise
License:        GPL
Url:            http://www.mailpiler.org/
Group:          Applications/Archiving

Source0:        https://bitbucket.org/jsuto/piler/downloads/%{name}-%{version}.tar.gz
Source1:        piler.service
Source2:        piler-tmpfile.conf

BuildRequires:  openssl-devel, tcp_wrappers-devel, poppler-utils, libzip-devel, catdoc, mysql-devel, tnef, unrtf, tre-devel
Requires:       openssl, tcp_wrappers, libzip, poppler-utils, catdoc, tnef, unrtf, tre
Provides:       libpiler.so()(64bit)

%if %{with init_systemd}
%{?systemd_requires: %systemd_requires}
%endif


%description
Piler gives you a secure central repository of emails providing the necessary information even if your mail servers are down.


%prep
%setup


%build
sed -e 's/ -o $(RUNNING_USER)//' \
    -e 's/ -g $(RUNNING_GROUP)//' \
    -i {,etc/,src/}Makefile.in
%configure \
  --prefix=/usr \
  --sysconfdir=/etc \
  --libdir=/usr/lib64 \
  --localstatedir=/var/lib \
  --libexecdir=/usr/share \
  --enable-starttls \
  --enable-tcpwrappers \
  --with-database=mysql \
  --with-piler-user=root
make clean all


%install
make install DESTDIR=%{buildroot}

# systemd
%if %{with init_systemd}
rm -rf %{buildroot}/etc/init.d %{buildroot}/var/lib/{run,piler}
%{__install} -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -Dm644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
mv %{_initddir}/{rc.,}piler
mv %{_initddir}/{rc.,}pilergetd
rm %{_initddir}/rc.searchd
%endif

# Gotta also copy over a few other things
mkdir -p %{buildroot}/var/www
cp -ar %{_topdir}/BUILD/%{name}-%{version}/webui %{buildroot}/var/www/piler

mkdir -p %{buildroot}/usr/share/piler
cp -r %{_topdir}/BUILD/%{name}-%{version}/contrib %{buildroot}/usr/share/piler


%files
%defattr(0755,root,root)
/usr/bin/pileraget
/usr/bin/pilerexport
/usr/bin/pilerget
/usr/bin/pilerpurge
/usr/bin/pilerimport
/usr/bin/reindex
/usr/bin/pilertest
/usr/sbin/piler
/usr/sbin/pilergetd
/usr/sbin/pilerconf
%defattr(-,root,root)
/etc/piler.conf
/etc/piler.conf.dist
/etc/sphinx.conf.dist
/usr/lib64/libpiler.a
/usr/lib64/libpiler.so
/usr/lib64/libpiler.so.0
/usr/lib64/libpiler.so.0.1.1
/usr/share/piler/daily-report.php
/usr/share/piler/generate_stats.php
/usr/share/piler/gmail-imap-import.php
/usr/share/piler/indexer.delta.sh
/usr/share/piler/indexer.main.sh
/usr/share/piler/import.sh
/usr/share/piler/postinstall.sh
/usr/share/piler/purge.sh
/usr/share/piler/db-mysql-root.sql.in
/usr/share/piler/db-mysql.sql
/usr/share/piler/automated-search.php
%docdir /usr/share/piler/contrib
/usr/share/piler/contrib/README
/usr/share/piler/contrib/imap/Makefile
/usr/share/piler/contrib/imap/Makefile.in
/usr/share/piler/contrib/imap/imap-seen.c
/usr/share/piler/contrib/mime/mime.types
/usr/share/piler/contrib/pop3/batch-import-without-removing.sh
/usr/share/piler/contrib/webserver/piler-apache-2.x.conf
/usr/share/piler/contrib/webserver/piler-nginx.conf
/var/www/piler
%if %{with init_systemd}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%else
%dir /var/lib/piler
%dir /var/lib/piler/tmp
%dir /var/lib/piler/sphinx
%dir /var/lib/piler/store
%dir /var/lib/piler/stat
%dir /var/lib/run/piler
%{_initddir}/piler
%{_initddir}/pilergetd
%endif


%post
%if %{with init_systemd}
%systemd_post %{name}.service
%tmpfiles_create %{name}.conf
%else
/sbin/chkconfig --add %{name}
chown -R piler:piler /var/lib/{run,piler}
%endif

echo /usr/lib > /etc/ld.so.conf.d/piler.conf
ldconfig
echo this is the postinstall stuff...
echo run /usr/libexec/piler/postinstall.sh manually to configure piler


%postun
%if %{with init_systemd}
%systemd_postun
%endif

userdel piler
groupdel piler


%pre
groupadd piler
useradd -g piler -s /bin/sh -d /var/piler piler
usermod -L piler
if [ -d /var/piler ]; then chmod 755 /var/piler; fi


%preun
%if %{with init_systemd}
%systemd_preun %{name}.service
%else
/sbin/service %{name} stop >/dev/null 2>&1
/sbin/chkconfig --del %{name}
%endif


%changelog
* Tue Feb 24 2015 Janos Suto
  - 1.1.1 release of piler

* Fri Nov  1 2013 Janos Suto
  - Fixed a bug causing issues when reading the retention|archiving_rules tables

* Fri Oct 25 2013 Janos Suto
  - First release of the rpm package based on build 846
