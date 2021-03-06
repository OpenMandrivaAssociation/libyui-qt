%define major 8
%define libname %mklibname yui %{major}-qt
%define develname %mklibname yui-qt -d

# (crazy) why do we use that old version ?
Name:		libyui-qt
Version:	2.47.1
Release:	3
Summary:	UI abstraction library - Qt plugin
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/libyui/libyui-qt
Source0:	https://github.com/libyui/libyui-qt/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libyui-qt-2.47.1-fix-build-against-qt-5.11.0.patch
Patch1:		libyui-qt-glibc-2.28.patch
Patch2:		try-to-fix-UI-crash.patch

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui) >= 3.1.2
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	texlive
BuildRequires:	graphviz
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(fontconfig)
Requires:	libyui

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Requires:	%{_lib}qt5x11extras5
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-qt = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-qt.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*


#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/KDE and Qt
Requires:	libyui-devel
Requires:	%{name} = %{EVRD}
Provides:	yui-qt-devel = %{EVRD}


%description -n %{develname}
This package provides headers files for libyui-qt development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/pkgconfig/libyui-qt.pc
%{_libdir}/cmake/libyui-qt

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -G Ninja

%ninja_build

%install
%ninja_install -C build
