%define name soqt
%define oname SoQt
%define version 1.4.1
%define release %mkrel 5

%define major 20
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d


Summary: SoQt interfaces Coin with the Qt GUI library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.coin3d.org/pub/coin/src/%{oname}-%{version}.tar.gz
Patch0:	soqt-lib.patch
License: GPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.coin3d.org/

BuildRequires: coin-devel
BuildRequires: kdelibs-devel

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
Provides: %{name}-devel = %{version}-%{release}
Provides: libsoqt-devel

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use SoQt.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%prep
%setup -q -n %oname-%version
%if "%{_lib}" == "lib64"
%patch0
%endif

%build

export QTDIR=%{_prefix}/lib/qt3/
# export LDFLAGS=$QTDIR/%{_lib}
%configure --disable-rpath
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root,0755)
%doc README FAQ AUTHORS NEWS
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_datadir}/Coin/conf/*
%{_datadir}/aclocal/*
%{_mandir}/man1/*
