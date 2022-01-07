#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-humanize
Version  : 3.13.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/8a/b6/e7d99d1cc225a069f3f7a906a213cb1a0148dac27119290c41dc257ffe53/humanize-3.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/b6/e7d99d1cc225a069f3f7a906a213cb1a0148dac27119290c41dc257ffe53/humanize-3.13.1.tar.gz
Summary  : Python humanize utilities
Group    : Development/Tools
License  : MIT
Requires: pypi-humanize-python = %{version}-%{release}
Requires: pypi-humanize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
# humanize
[![PyPI version](https://img.shields.io/pypi/v/humanize.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/humanize/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/humanize.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/humanize/)
[![Documentation Status](https://readthedocs.org/projects/python-humanize/badge/?version=latest)](https://python-humanize.readthedocs.io/en/latest/?badge=latest)
[![PyPI downloads](https://img.shields.io/pypi/dm/humanize.svg)](https://pypistats.org/packages/humanize)
[![GitHub Actions status](https://github.com/jmoiron/humanize/workflows/Test/badge.svg)](https://github.com/jmoiron/humanize/actions)
[![codecov](https://codecov.io/gh/hugovk/humanize/branch/master/graph/badge.svg)](https://codecov.io/gh/hugovk/humanize)
[![MIT License](https://img.shields.io/github/license/jmoiron/humanize.svg)](LICENCE)
[![Tidelift](https://tidelift.com/badges/package/pypi/humanize)](https://tidelift.com/subscription/pkg/pypi-humanize?utm_source=pypi-humanize&utm_medium=badge)

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
%setup -q -n humanize-3.13.1
cd %{_builddir}/humanize-3.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638830398
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
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
