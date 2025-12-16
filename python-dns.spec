%global pypi_name dnspython
%global py_package_name dns

Name:		python-%{py_package_name}
Version:	2.8.0
Release:	1
Summary:	DNS toolkit for Python

License:	MIT
URL:		https://www.dnspython.org

Source0:	https://files.pythonhosted.org/packages/source/d/dnspython/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

# Renamed 2025/12/16 after 6.0
%rename python3-%{name}

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%prep -a
# strip exec permissions so that we don't pick up dependencies from docs
find examples -type f | xargs chmod a-x

%files
%license LICENSE
%doc README.md examples
%{python_sitelib}/%{py_package_name}
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
