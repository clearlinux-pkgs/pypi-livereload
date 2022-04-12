#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-livereload
Version  : 2.6.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/bd/60/6640b819e858562ef6684abac60593b7369fe0a8a064df426d3ab0ab894d/livereload-2.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/60/6640b819e858562ef6684abac60593b7369fe0a8a064df426d3ab0ab894d/livereload-2.6.3.tar.gz
Summary  : Python LiveReload is an awesome tool for web developers
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-livereload-bin = %{version}-%{release}
Requires: pypi-livereload-license = %{version}-%{release}
Requires: pypi-livereload-python = %{version}-%{release}
Requires: pypi-livereload-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)
BuildRequires : pypi(tornado)

%description
==========
        
        This is a brand new LiveReload in version 2.0.0.

%package bin
Summary: bin components for the pypi-livereload package.
Group: Binaries
Requires: pypi-livereload-license = %{version}-%{release}

%description bin
bin components for the pypi-livereload package.


%package license
Summary: license components for the pypi-livereload package.
Group: Default

%description license
license components for the pypi-livereload package.


%package python
Summary: python components for the pypi-livereload package.
Group: Default
Requires: pypi-livereload-python3 = %{version}-%{release}

%description python
python components for the pypi-livereload package.


%package python3
Summary: python3 components for the pypi-livereload package.
Group: Default
Requires: python3-core
Provides: pypi(livereload)
Requires: pypi(six)
Requires: pypi(tornado)

%description python3
python3 components for the pypi-livereload package.


%prep
%setup -q -n livereload-2.6.3
cd %{_builddir}/livereload-2.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649780701
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-livereload
cp %{_builddir}/livereload-2.6.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-livereload/765c9f569ab66e6eea58a640c9de3d20e297d687
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/livereload

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-livereload/765c9f569ab66e6eea58a640c9de3d20e297d687

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
