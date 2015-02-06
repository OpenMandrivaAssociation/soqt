%define name soqt
%define oname SoQt
%define version 1.5.0
%define release   4

%define major 20
%define libname %mklibname %name %major
%define libnamedev %mklibname %name -d


Summary: Interfaces Coin with the Qt GUI library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.coin3d.org/pub/coin/src/%{oname}-%{version}.tar.gz
Patch0:	soqt-lib.patch
License: GPLv2
Group: System/Libraries
URL: http://www.coin3d.org/

BuildRequires: coin-devel
BuildRequires: pkgconfig(Qt3Support)

%description 
SoQt interfaces Coin with the Qt GUI library.

%package -n %{libname}
Summary: Main library for SoQt
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with SoQt.

%package -n %{libnamedev}
Summary: Headers for developing programs that will use SoQt
Group: Development/C++
Requires: %{libname} = %{version}
Requires: coin-devel
Requires: libqt4-devel
Provides: %{name}-devel = %{version}-%{release}
Provides: libsoqt-devel
Obsoletes: %{_lib}soqt20-devel

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use SoQt.

%prep
%setup -q -n %oname-%version
%if "%{_lib}" == "lib64"
%patch0
%endif

%build

QTDIR="%qt4dir"
export QTDIR
# export LDFLAGS=$QTDIR/%{_lib}
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root,0755)
%doc README FAQ AUTHORS NEWS
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/SoQt.pc
%{_includedir}/*
%{_datadir}/Coin/conf/*
%{_datadir}/aclocal/*
%{_mandir}/man1/*
