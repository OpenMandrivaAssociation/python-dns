Name:           python-dns
Version:        2.3.5
Release:        %mkrel 1
Epoch:          0
Summary:        Python module for DNS (Domain Name Service)
Group:          Development/Python
License:        Python Software Foundation License
URL:            http://pydns.sourceforge.net/
Source0:        pydns-%{version}.tar.gz
Provides:       pydns = %{epoch}:%{version}-%{release}
Provides:       python-pydns = %{epoch}:%{version}-%{release}
Provides:       python-DNS = %{epoch}:%{version}-%{release}
BuildArch:      noarch
%py_requires -d
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a another release of the pydns code, as originally written by
Guido van Rossum, and with a hopefully nicer API bolted over the
top of it by Anthony Baxter <anthony@interlink.com.au>.

This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

%prep
%setup -q -n pydns-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O2 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CREDITS.txt PKG-INFO README-guido.txt README.txt
%{python_sitelib}/*



%changelog
* Wed Mar 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:2.3.5-1mdv2011.0
+ Revision: 647779
- new version

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0:2.3.4-2mdv2011.0
+ Revision: 593084
- rebuild for py2.7

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:2.3.4-1mdv2010.1
+ Revision: 496368
- update to new version 2.3.4

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:2.3.3-3mdv2010.0
+ Revision: 442098
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0:2.3.3-2mdv2009.1
+ Revision: 323562
- rebuild

* Thu Aug 28 2008 Frederik Himpe <fhimpe@mandriva.org> 0:2.3.3-1mdv2009.0
+ Revision: 276939
- update to new version 2.3.3

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:2.3.1-4mdv2009.0
+ Revision: 259564
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:2.3.1-3mdv2009.0
+ Revision: 247403
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 30 2007 David Walluck <walluck@mandriva.org> 0:2.3.1-1mdv2008.1
+ Revision: 103717
- import python-dns


