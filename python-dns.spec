%global pypi_name dnspython
%global py_package_name dns

# Disable dependency generator until it has test code
%{?python_disable_dependency_generator}

Name:           python-%{py_package_name}
Version:        2.1.0
Release:        3
Summary:        DNS toolkit for Python

License:        MIT
URL:            https://www.dnspython.org

Source0:        https://files.pythonhosted.org/packages/source/d/dnspython/%{pypi_name}-%{version}.zip

# A no-op typing module for import compatibility
# This avoids the build dependency on python2-typing
Source1:        typing.py

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-setuptools

%global _description %{expand:
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.
}

%description
%_description

%package -n python3-%{py_package_name}
Summary:        %{summary}
BuildRequires:  python3-devel
Provides:	python-%{py_package_name} = %{EVRD}
Provides:	python-%{pypi_name} = %{EVRD}

%description -n python3-%{py_package_name}
%_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# strip exec permissions so that we don't pick up dependencies from docs
find examples -type f | xargs chmod a-x

%build
%py3_build

%install
%py3_install

%files -n python3-%{py_package_name}
%license LICENSE
%doc README.md examples
%{python3_sitelib}/%{py_package_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
