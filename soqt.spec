%define tarname		SoQt

%define major		20
%define libname		%mklibname %name %major
%define libnamedev	%mklibname %name -d

Summary:		Interfaces Coin with the Qt GUI library
Name:			soqt
Version:		1.6.0
Release:		1
Source0:	https://bitbucket.org/Coin3D/soqt/downloads/soqt-%{version}-src.zip
License:		GPLv2
Group:			System/Libraries
URL:			http://www.coin3d.org/

Patch0:         SoQt-1.6.0-pkgconf.patch
Patch1:         SoQt-1.6.0-cmake.patch
BuildRequires:  qt5-qtbase-devel

%description
SoQt, like Coin and Qt, provides the programmer with a high-level application
programmer's interface (API) in C++. The library primarily includes a
class-hierarchy of viewer components of varying functionality and complexity,
with various modes for the end-user to control the 3D-scene camera interaction.

%package -n %{libname}
Summary:		Main library for SoQt
Group:			System/Libraries
Provides:		%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with SoQt.

%package -n %{libnamedev}
Summary:		Headers for developing programs that will use SoQt
Group:			Development/C++
Requires:		%{libname} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}
Provides:		%{tarname}-devel = %{version}-%{release}
Obsoletes:		%{_lib}soqt20-devel < 1.5.0-4

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use SoQt.

%prep
%autosetup -p1 -n soqt

%build
%cmake
%make_build

%install
%make_install -C build

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/libSoQt.so.%{version}*

%files -n %{libnamedev}
%doc README FAQ AUTHORS NEWS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/SoQt/materials/
%{_libdir}/cmake/SoQt-%{version}/*.cmake
