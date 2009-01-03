Name:           python-dns
Version:        2.3.3
Release:        %mkrel 2
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

