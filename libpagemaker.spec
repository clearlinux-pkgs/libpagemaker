#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpagemaker
Version  : 0.0.4
Release  : 3
URL      : https://dev-www.libreoffice.org/src/libpagemaker-0.0.4.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libpagemaker-0.0.4.tar.xz
Summary  : Library for importing and converting PageMaker Documents
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libpagemaker-bin
Requires: libpagemaker-lib
Requires: libpagemaker-license
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)

%description
libpagemaker is a library and a set of tools for reading and converting
Aldus/Macromedia/Adobe PageMaker documents. Supported are documents
created by versions 6-7 (both Windows and Mac). Documents created by
older versions might work, but they are untested.

%package bin
Summary: bin components for the libpagemaker package.
Group: Binaries
Requires: libpagemaker-license

%description bin
bin components for the libpagemaker package.


%package dev
Summary: dev components for the libpagemaker package.
Group: Development
Requires: libpagemaker-lib
Requires: libpagemaker-bin
Provides: libpagemaker-devel

%description dev
dev components for the libpagemaker package.


%package doc
Summary: doc components for the libpagemaker package.
Group: Documentation

%description doc
doc components for the libpagemaker package.


%package lib
Summary: lib components for the libpagemaker package.
Group: Libraries
Requires: libpagemaker-license

%description lib
lib components for the libpagemaker package.


%package license
Summary: license components for the libpagemaker package.
Group: Default

%description license
license components for the libpagemaker package.


%prep
%setup -q -n libpagemaker-0.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534634476
%configure --disable-static --disable-werror
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534634476
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libpagemaker
cp COPYING %{buildroot}/usr/share/doc/libpagemaker/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pmd2raw
/usr/bin/pmd2svg
/usr/bin/pmd2text

%files dev
%defattr(-,root,root,-)
/usr/include/libpagemaker-0.0/libpagemaker/PMDocument.h
/usr/include/libpagemaker-0.0/libpagemaker/libpagemaker.h
/usr/lib64/libpagemaker-0.0.so
/usr/lib64/pkgconfig/libpagemaker-0.0.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libpagemaker/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpagemaker-0.0.so.0
/usr/lib64/libpagemaker-0.0.so.0.0.4

%files license
%defattr(-,root,root,-)
/usr/share/doc/libpagemaker/COPYING
