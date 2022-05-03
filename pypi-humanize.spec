#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-humanize
Version  : 4.1.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/bb/68/c8be852a42c3b0364ad256a8cb41ab619d445b812aa16f94c9d16b042d74/humanize-4.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/68/c8be852a42c3b0364ad256a8cb41ab619d445b812aa16f94c9d16b042d74/humanize-4.1.0.tar.gz
Summary  : Python humanize utilities
Group    : Development/Tools
License  : MIT
Requires: pypi-humanize-license = %{version}-%{release}
Requires: pypi-humanize-python = %{version}-%{release}
Requires: pypi-humanize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# humanize
[![PyPI version](https://img.shields.io/pypi/v/humanize.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/humanize/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/humanize.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/humanize/)
[![Documentation Status](https://readthedocs.org/projects/python-humanize/badge/?version=latest)](https://python-humanize.readthedocs.io/en/latest/?badge=latest)
[![PyPI downloads](https://img.shields.io/pypi/dm/humanize.svg)](https://pypistats.org/packages/humanize)
[![GitHub Actions status](https://github.com/python-humanize/humanize/workflows/Test/badge.svg)](https://github.com/python-humanize/humanize/actions)
[![codecov](https://codecov.io/gh/python-humanize/humanize/branch/main/graph/badge.svg)](https://codecov.io/gh/python-humanize/humanize)
[![MIT License](https://img.shields.io/github/license/python-humanize/humanize.svg)](LICENCE)
[![Tidelift](https://tidelift.com/badges/package/pypi/humanize)](https://tidelift.com/subscription/pkg/pypi-humanize?utm_source=pypi-humanize&utm_medium=badge)

%package license
Summary: license components for the pypi-humanize package.
Group: Default

%description license
license components for the pypi-humanize package.


%package python
Summary: python components for the pypi-humanize package.
Group: Default
Requires: pypi-humanize-python3 = %{version}-%{release}

%description python
python components for the pypi-humanize package.


%package python3
Summary: python3 components for the pypi-humanize package.
Group: Default
Requires: python3-core
Provides: pypi(humanize)

%description python3
python3 components for the pypi-humanize package.


%prep
%setup -q -n humanize-4.1.0
cd %{_builddir}/humanize-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651591567
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-humanize
cp %{_builddir}/humanize-4.1.0/LICENCE %{buildroot}/usr/share/package-licenses/pypi-humanize/bb7ef51103bdeb7a12af17acbf39fda04e6e354e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-humanize/bb7ef51103bdeb7a12af17acbf39fda04e6e354e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
