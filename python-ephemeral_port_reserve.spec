#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python module and utility to reserve an ephemeral port
Summary(pl.UTF-8):	Moduł i narzędzie pythonowe do rezerwowania wolnego portu
Name:		python-ephemeral_port_reserve
Version:	1.1.4
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ephemeral-port-reserve/
Source0:	https://files.pythonhosted.org/packages/source/e/ephemeral-port-reserve/ephemeral_port_reserve-%{version}.tar.gz
# Source0-md5:	edfd1f2b984da8a6bc28980663e0c849
URL:		https://pypi.org/project/ephemeral-port-reserve/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module and utility to bind to an ephemeral port, force it into
the TIME_WAIT state, and unbind it.

%description -l pl.UTF-8
Moduł i narzędzie pythonowe przypinające się do wolnego portu,
umieszczające go w stanie TIME_WAIT i odpinające się od niego.

%package -n python3-ephemeral_port_reserve
Summary:	Python module and utility to reserve an ephemeral port
Summary(pl.UTF-8):	Moduł i narzędzie pythonowe do rezerwowania wolnego portu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-ephemeral_port_reserve
Python module and utility to bind to an ephemeral port, force it into
the TIME_WAIT state, and unbind it.

%description -n python3-ephemeral_port_reserve -l pl.UTF-8
Moduł i narzędzie pythonowe przypinające się do wolnego portu,
umieszczające go w stanie TIME_WAIT i odpinające się od niego.

%package apidocs
Summary:	API documentation for Python ephemeral_port_reserve module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona ephemeral_port_reserve
Group:		Documentation

%description apidocs
API documentation for Python ephemeral_port_reserve module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona ephemeral_port_reserve.

%prep
%setup -q -n ephemeral_port_reserve-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/ephemeral-port-reserve{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/ephemeral-port-reserve{,-3}
ln -sf ephemeral-port-reserve-3 $RPM_BUILD_ROOT%{_bindir}/ephemeral-port-reserve
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/ephemeral-port-reserve-2
%{py_sitescriptdir}/ephemeral_port_reserve.py[co]
%{py_sitescriptdir}/ephemeral_port_reserve-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ephemeral_port_reserve
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/ephemeral-port-reserve
%attr(755,root,root) %{_bindir}/ephemeral-port-reserve-3
%{py3_sitescriptdir}/ephemeral_port_reserve.py
%{py3_sitescriptdir}/__pycache__/ephemeral_port_reserve.cpython-*.py[co]
%{py3_sitescriptdir}/ephemeral_port_reserve-%{version}-py*.egg-info
%endif
