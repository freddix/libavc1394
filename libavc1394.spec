Summary:	Programming interface to the 1394 AV/C specification
Name:		libavc1394
Version:	0.5.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libavc1394/%{name}-%{version}.tar.gz
# Source0-md5:	caf0db059d8b8d35d6f08e6c0e1c7dfe
URL:		http://sourceforge.net/projects/libavc1394/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libraw1394-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libavc1394 is a programming interface to the AV/C specification from
the 1394 Trade Association. AV/C stands for Audio/Video Control.
Currently, applications use the library to control the tape transport
mechanism on DV camcorders. However, there are many devices and
functions of devices that can be controlled via AV/C. Eventually, the
library will be expanded to implement more of the specification and to
provide high level interfaces to various devices.

%package devel
Summary:	libavc1394 header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw1394-devel

%description devel
libavc1394 header files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libavc1394.so.?
%attr(755,root,root) %ghost %{_libdir}/librom1394.so.?
%attr(755,root,root) %{_libdir}/libavc1394.so.*.*.*
%attr(755,root,root) %{_libdir}/librom1394.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavc1394.so
%attr(755,root,root) %{_libdir}/librom1394.so
%{_includedir}/libavc1394
%{_pkgconfigdir}/libavc1394.pc

