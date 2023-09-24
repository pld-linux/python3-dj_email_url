Summary:	Use an URL to configure email backend settings in your Django Application
Summary(pl.UTF-8):	Konfigurowanie ustawień backendu e-mail w aplikacji Django przy użyciu URL-a
Name:		python3-dj_email_url
Version:	1.0.6
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dj-email-url/
Source0:	https://files.pythonhosted.org/packages/source/d/dj-email-url/dj-email-url-%{version}.tar.gz
# Source0-md5:	4005c75282a07cde7aac787ed51277df
URL:		https://pypi.org/project/dj-email-url/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
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

%prep
%setup -q -n dj-email-url-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%{py3_sitescriptdir}/dj_email_url.py
%{py3_sitescriptdir}/__pycache__/dj_email_url.cpython-*.py[co]
%{py3_sitescriptdir}/dj_email_url-%{version}-py*.egg-info
