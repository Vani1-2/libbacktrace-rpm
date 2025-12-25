Name:           libbacktrace
Version:        1.0
Release:        3%{?dist}
Summary:        A C library to produce symbolic backtraces

License:        BSD
URL:            https://github.com/ianlancetaylor/libbacktrace
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make

%description
A C library that may be linked into a C/C++ program to produce symbolic 
backtraces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries, header files, and pkg-config
files for developing applications that use %{name}.

%prep
%autosetup

%build
autoreconf -fiv
%configure --enable-shared --disable-static --with-pic
%make_build

%install
%make_install


find %{buildroot} -name '*.la' -delete
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/libbacktrace.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libbacktrace
Description: A C library to produce symbolic backtraces
Version: %{version}
Libs: -L\${libdir} -lbacktrace
Cflags: -I\${includedir}
EOF

%files
%license LICENSE
%{_libdir}/libbacktrace.so.0*

%files devel
%{_includedir}/backtrace.h
%{_includedir}/backtrace-supported.h
%{_libdir}/libbacktrace.so
%{_libdir}/pkgconfig/libbacktrace.pc

%changelog
* Thu Dec 25 2025 Vani1-2 <giovannirafanan609@gmail.com> - 1.0-3
- fixed build errors caused by mismatched tar.gz
