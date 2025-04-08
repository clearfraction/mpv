%global gitdate 20250325
%global commit e48ac7ce08462f5e33af6ef9deeac6fa87eef01e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name     : mpv
Version  : 0.40.0
Release  : %{gitdate}.%{shortcommit}
URL      : https://github.com/mpv-player/mpv
Source0  : %{url}/archive/%{commit}/mpv-%{shortcommit}.tar.gz
#Source   : https://github.com/mpv-player/mpv/archive/refs/heads/master.zip 
Summary  : media player
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: ffmpeg-libs
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
#Requires: mpv-filemap = %%{version}-%%{release}
BuildRequires : buildreq-meson
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : SPIRV-Cross-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXpresent-dev
BuildRequires : libXv-dev
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
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xv)
BuildRequires : zlib-dev
BuildRequires : SDL2-dev
BuildRequires : LuaJIT-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libarchive)
BuildRequires : pipewire-dev
BuildRequires : shaderc-dev uchardet-dev zimg-dev SPIRV-Headers-dev
BuildRequires : pkgconfig(vapoursynth)
BuildRequires : pkgconfig(vapoursynth-script)
BuildRequires : libdisplay-info-dev

# fonts-related
BuildRequires : v4l-utils-dev fontconfig-dev fribidi-dev harfbuzz-dev libpng-dev


%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.
 
%package bin
Summary: bin components for the mpv package.
Group: Binaries
Requires: mpv-data = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
#Requires: mpv-filemap = %%{version}-%%{release}

 
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
#Requires: mpv-filemap = %%{version}-%%{release}

 
%description lib
lib components for the mpv package.
 
 
%package license
Summary: license components for the mpv package.
Group: Default
 
%description license
license components for the mpv package.


%prep
%setup -q -n mpv-%{commit}
git config --global --add safe.directory /home

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export LDFLAGS="-Wl,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64,-rpath=/usr/lib64 "
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "

meson --libdir=lib64 --prefix=/usr --buildtype=plain --auto-features=auto       \
  -Dcdda=disabled             \
  -Dlibmpv=true              \
  -Ddvbin=disabled            \
  -Ddvdnav=disabled           \
  -Dopenal=disabled builddir      
      
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rvf %{buildroot}/usr/share/doc

 
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
/usr/share/icons/hicolor/128x128/apps/mpv.png
/usr/share/icons/hicolor/scalable/apps/mpv.svg
/usr/share/icons/hicolor/symbolic/apps/mpv-symbolic.svg
/usr/share/zsh/site-functions/_mpv
/usr/share/bash-completion/completions/mpv
/usr/share/fish/vendor_completions.d/mpv.fish
/usr/share/metainfo/mpv.metainfo.xml
 
%files dev
%defattr(-,root,root,-)
/usr/include/mpv/client.h
/usr/include/mpv/render.h
/usr/include/mpv/render_gl.h
/usr/include/mpv/stream_cb.h
/usr/lib64/libmpv.so*
/usr/lib64/pkgconfig/mpv.pc
 
%files doc
%defattr(0644,root,root,0755)
 
%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpv.so.*
 
%files license
%defattr(0644,root,root,0755)

