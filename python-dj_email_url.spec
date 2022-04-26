#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use an URL to configure email backend settings in your Django Application
Summary(pl.UTF-8):	Konfigurowanie ustawień backendu e-mail w aplikacji Django przy użyciu URL-a
Name:		python-dj_email_url
# keep 0.x here for python2 support
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dj-email-url/
Source0:	https://files.pythonhosted.org/packages/source/d/dj-email-url/dj-email-url-%{version}.tar.gz
# Source0-md5:	d509c9e369fb7762055590c6dbd67747
URL:		https://pypi.org/project/dj-email-url/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows to utilize the 12factor inspired EMAIL_URL
environment variable to configure the email backend in a Django
application.

%description -l pl.UTF-8
Ten moduł pozwala na konfigurowanie backendu e-mail w aplikacji Django
przy użyciu zmiennej środowiskowej EMAIL_URL, zainspirowanej przez
12factor.

%package -n python3-dj_email_url
Summary:	Use an URL to configure email backend settings in your Django Application
Summary(pl.UTF-8):	Konfigurowanie ustawień backendu e-mail w aplikacji Django przy użyciu URL-a
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-dj_email_url
This module allows to utilize the 12factor inspired EMAIL_URL
environment variable to configure the email backend in a Django
application.

%description -n python3-dj_email_url -l pl.UTF-8
Ten moduł pozwala na konfigurowanie backendu e-mail w aplikacji Django
przy użyciu zmiennej środowiskowej EMAIL_URL, zainspirowanej przez
12factor.

%prep
%setup -q -n dj-email-url-%{version}

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
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%{py_sitescriptdir}/dj_email_url.py[co]
%{py_sitescriptdir}/dj_email_url-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dj_email_url
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%{py3_sitescriptdir}/dj_email_url.py
%{py3_sitescriptdir}/__pycache__/dj_email_url.cpython-*.py[co]
%{py3_sitescriptdir}/dj_email_url-%{version}-py*.egg-info
%endif
