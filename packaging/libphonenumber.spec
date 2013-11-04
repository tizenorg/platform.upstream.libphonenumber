Name:           libphonenumber
Version:        5.3.2
Release:        1
License:        Apache-2.0
Summary:        A library for manipulating international phone numbers
Url:            http://code.google.com/p/libphonenumber/
Group:          Social & Content/Libraries
Source:         libphonenumber-%{version}.tgz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel
BuildRequires:  re2-devel
BuildRequires:  protobuf-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(icu-i18n)

%description
Google's common Java, C++ and Javascript library for parsing,
formatting, storing and validating international phone numbers. The
Java version is optimized for running on smartphones, and is used by
the Android framework since 4.0 (Ice Cream Sandwich).

%package devel
Summary:        Devel package for library
Group:          Social & Content/Libraries
Requires:       libphonenumber = %{version}
Requires:       protobuf-devel

%description devel
Google's common Java, C++ and Javascript library for parsing,
formatting, storing and validating international phone numbers. The
Java version is optimized for running on smartphones, and is used by
the Android framework since 4.0 (Ice Cream Sandwich).

%prep
%setup -q -n libphonenumber

%build
%cmake \
   -DBUILD_GEOCODER=OFF \
   -DCMAKE_SKIP_RPATH=ON \
   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
   cpp

%{__make} %{?jobs:-j%jobs}

%install
%{__make} DESTDIR=%{buildroot} install
rm %{buildroot}/%{_libdir}/*.a

%post   -n libphonenumber -p /sbin/ldconfig

%postun -n libphonenumber -p /sbin/ldconfig


%files -n libphonenumber
%defattr(-, root, root, -)
%doc AUTHORS
%license LICENSE
%{_libdir}/libphonenumber.so.5
%{_libdir}/libphonenumber.so.5.3

# Needs to be packaged separately should compilation of it
# get enabled with -DBUILD_GEOCODER=ON.
# %{_libdir}/libgeocoding.so.5
# %{_libdir}/libgeocoding.so.5.3

%files devel
%defattr(-, root, root, -)
%{_includedir}/phonenumbers
%{_includedir}/base
%{_libdir}/libphonenumber.so
# %{_libdir}/libgeocoding.so
