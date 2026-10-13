%define module immutabledict
%bcond tests 1

Name:		python-immutabledict
Version:	4.3.1
Release:	3
Summary:	Immutable wrapper around dictionaries (a fork of frozendict)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/immutabledict/
Source0:	https://files.pythonhosted.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Immutable wrapper around dictionaries (a fork of frozendict)

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# test_performance compares wall time with a builtin dict and fails when
# the builder is busy.
pytest -k 'not test_performance'
%endif

%files
%doc README.md
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
