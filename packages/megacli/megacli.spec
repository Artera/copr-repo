Summary:	LSI Logic MegaRAID Linux MegaCLI utility
Name:		megacli
Version:	8.07.14
Release:	1%{?dist}
License:	Proprietary
Group:		Applications/System
Source0:	https://downloads.artera.it/8-07-14_MegaCLI.zip
Source1:	LICENSE
URL:        https://www.broadcom.com/support/download-search/?pg=Storage+Adapters,+Controllers,+and+ICs&pf=RAID+Controller+Cards&pn=&pa=Management+Software+and+Tools&po=&dk=megacli+linux
Requires:	sysfsutils
ExclusiveArch:	x86_64
BuildRoot:	%{tmpdir}/%{name}-%{version}-%{release}-root

%description
Tool to control MegaRAID controllers:
- MegaRAID SAS 9270-8i
- MegaRAID SAS 9271-4i
- MegaRAID SAS 9271-8i
- MegaRAID SAS 9271-8iCC
- MegaRAID SAS 9286-8e
- MegaRAID SAS 9286CV-8e
- MegaRAID SAS 9286CV-8eCC
- MegaRAID SAS 9265-8i
- MegaRAID SAS 9285-8e
- MegaRAID SAS 9240-4i
- MegaRAID SAS 9240-8i
- MegaRAID SAS 9260-4i
- MegaRAID SAS 9260CV-4i
- MegaRAID SAS 9260-8i
- MegaRAID SAS 9260CV-8i
- MegaRAID SAS 9260DE-8i
- MegaRAID SAS 9261-8i
- MegaRAID SAS 9280-4i4e
- MegaRAID SAS 9280-8e
- MegaRAID SAS 9280DE-8e
- MegaRAID SAS 9280-24i4e
- MegaRAID SAS 9280-16i4e
- MegaRAID SAS 9260-16i
- MegaRAID SAS 9266-4i
- MegaRAID SAS 9266-8i
- MegaRAID SAS 9285CV-8e
- MegaRAID SAS 8704ELP
- MegaRAID SAS 8704EM2
- MegaRAID SAS 8708ELP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2
- MegaRAID SAS 8888ELP
- MegaRAID SAS 8308ELP*
- MegaRAID SAS 8344ELP*
- MegaRAID SAS 84016E*
- MegaRAID SAS 8408E*
- MegaRAID SAS 8480E*
- MegaRAID SATA 300-8ELP*

* These older controllers should work but have not been tested.

%prep
%setup -qc
rpm2cpio Linux/MegaCli-%{version}*.rpm | cpio -i -d
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}}
install -p opt/MegaRAID/MegaCli/MegaCli64 $RPM_BUILD_ROOT%{_sbindir}/megacli
install -p opt/MegaRAID/MegaCli/libstorelibir-2.so.* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_sbindir}/megacli
%{_libdir}/libstorelibir-2.so.*
