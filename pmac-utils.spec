%define	name	pmac-utils
%define	version	2.0
%define	release	%mkrel 6

Summary:	PowerPC Linux system utilities
Name:		pmac-utils
Version:	%{version}
Release:	%{release}
Group:		System/Configuration/Hardware
License:	GPL
Source:		pmac-utils-%{version}.tar.bz2
Patch0:		nvsetenv-man-patch.bz2
Patch1:		pmac-utils-mousemode-patch.bz2
Patch2:		pmac-utils-makefile-patch.bz2
BuildRequires:	sgml-tools linuxdoc-tools
ExclusiveArch:	ppc

%description
PPC-Linux-specific applications including macos, mousemode, nvsetenv, nvvideo.

%prep

%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std man8dir=%{_mandir}/man8
rm -f $RPM_BUILD_ROOT{/sbin/,%{_mandir}/man8/}macos*

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -c /dev/nvram ]; then
	echo "Creating /dev/nvram ..."
	mknod /dev/nvram c 10 144
	chmod 644 /dev/nvram
fi

%files
%defattr(-, root, root) 
/sbin/mousemode
/sbin/nvsetenv
/sbin/nvvideo
%{_mandir}/man8/mousemode.8*
%{_mandir}/man8/nvsetenv.8*
%{_mandir}/man8/nvvideo.8*

