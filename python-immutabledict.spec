Name:		python-immutabledict
Version:	4.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/i/immutabledict/immutabledict-%{version}.tar.gz
Summary:	Immutable wrapper around dictionaries (a fork of frozendict)
URL:		https://pypi.org/project/immutabledict/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Immutable wrapper around dictionaries (a fork of frozendict)

%prep
%autosetup -p1 -n immutabledict-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/immutabledict
%{py_sitedir}/immutabledict-*.*-info
