Summary:	Qt IPod Interface library
#Summary(pl.UTF-8):	
Name:		libqtpod
Version:	0.4.2
Release:	0.1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/kpod/%{name}-%{version}.tar.bz2
# Source0-md5:	88af1193a2ef9c3b37f034cf9e94f5d3
Patch0:		%{name}-utils.patch
URL:		http://sourceforge.net/projects/kpod/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	qt-devel
BuildRequires:	qmake
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt IPod library.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for libqtpod development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libqtpod
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libqtpod development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libqtpod.

%prep
%setup -q
%patch -P0 -p1

%build
QTDIR=/usr qmake
QTDIR=/usr \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}

install src/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install src/%{name}*.so* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so.*.*
#%attr(755,root,root) %{_libdir}/%{name}.so.?.?
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
