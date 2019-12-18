Name     : mpv
Version  : 0.30.0
Release  : 1
URL      : https://github.com/mpv-player/mpv
Source0  : https://github.com/mpv-player/mpv/archive/v0.30.0.tar.gz
Patch1   : https://github.com/clearlinux-pkgs/mpv/raw/master/0001-waf-add-waf-as-a-patch-for-ClearLinux.patch
Patch2   : https://github.com/clearlinux-pkgs/mpv/raw/master/0002-Makefile-quick-wrapper-for-waf.patch
Summary  : mpv media player client library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : SPIRV-Headers-dev
BuildRequires : libX11-dev
BuildRequires : libva-dev
BuildRequires : mesa-dev
BuildRequires : ffmpeg-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libass)
BuildRequires : pkgconfig(libplacebo)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : zlib-dev

 
%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.
 
%package bin
Summary: bin components for the mpv package.
Group: Binaries
Requires: mpv-data = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
 
%description bin
bin components for the mpv package.
 
 
%package data
Summary: data components for the mpv package.
Group: Data
 
%description data
data components for the mpv package.
 
 
%package dev
Summary: dev components for the mpv package.
Group: Development
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Provides: mpv-devel = %{version}-%{release}
Requires: mpv = %{version}-%{release}
 
%description dev
dev components for the mpv package.
 
 
%package doc
Summary: doc components for the mpv package.
Group: Documentation
 
%description doc
doc components for the mpv package.
 
 
%package lib
Summary: lib components for the mpv package.
Group: Libraries
Requires: mpv-data = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
 
%description lib
lib components for the mpv package.
 
 
%package license
Summary: license components for the mpv package.
Group: Default
 
%description license
license components for the mpv package.
 
 
%prep
%setup -q -n mpv-%{version}
%patch1 -p1
%patch2 -p1
 
%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563233323
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}
 
 
%install
export SOURCE_DATE_EPOCH=1563233323
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mpv
cp Copyright %{buildroot}/usr/share/package-licenses/mpv/Copyright
cp LICENSE.GPL %{buildroot}/usr/share/package-licenses/mpv/LICENSE.GPL
cp LICENSE.LGPL %{buildroot}/usr/share/package-licenses/mpv/LICENSE.LGPL
%make_install
 
%files
%defattr(-,root,root,-)
 
%files bin
%defattr(-,root,root,-)
/usr/bin/mpv
 
%files data
%defattr(-,root,root,-)
/usr/share/applications/mpv.desktop
/usr/share/icons/hicolor/16x16/apps/mpv.png
/usr/share/icons/hicolor/32x32/apps/mpv.png
/usr/share/icons/hicolor/64x64/apps/mpv.png
/usr/share/icons/hicolor/scalable/apps/mpv.svg
/usr/share/icons/hicolor/symbolic/apps/mpv-symbolic.svg
/usr/share/zsh/site-functions/_mpv
 
%files dev
%defattr(-,root,root,-)
/usr/include/mpv/client.h
/usr/include/mpv/opengl_cb.h
/usr/include/mpv/qthelper.hpp
/usr/include/mpv/render.h
/usr/include/mpv/render_gl.h
/usr/include/mpv/stream_cb.h
/usr/lib64/libmpv.so*
/usr/lib64/pkgconfig/mpv.pc
 
%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/mpv/*
 
%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpv.so.*
 
%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpv/Copyright
/usr/share/package-licenses/mpv/LICENSE.GPL
/usr/share/package-licenses/mpv/LICENSE.LGPL
