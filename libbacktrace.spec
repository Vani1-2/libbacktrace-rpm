Name:           libbacktrace
Version:        1.0
Release:        1%{?dist}
Summary:        A C library to produce symbolic backtraces
License:        BSD
URL:            https://github.com/ianlancetaylor/libbacktrace
Source0:        https://github.com/ianlancetaylor/%{name}/archive/master.zip

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  libtool

%description
A C library that may be linked into a C/C++ program to produce symbolic 
backtraces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-master

%build
%configure --enable-shared --disable-static --with-pic
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license LICENSE
%{_libdir}/libbacktrace.so.0*

%files devel
%{_includedir}/backtrace.h
%{_includedir}/backtrace-supported.h
%{_libdir}/libbacktrace.so

%changelog
* Thu Dec 25 2025 Vani1-2 <giovannirafanan609@gmail.com> - 1.0-1
- Initial package
