Summary: Library for error values used by GnuPG components
Name: libgpg-error
Version: 1.10
Release: 1
URL: ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
Source2: wk@g10code.com
Patch0: libgpg-error-1.10-adding-pc.patch
Group: System/Libraries
License: LGPLv2+
BuildRequires: gawk, gettext
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep
%setup -q
%patch0 -p1
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpg-error-config.in

%build
%reconfigure --disable-static
make

%install
rm -fr $RPM_BUILD_ROOT
%make_install
rm -r $RPM_BUILD_ROOT/%{_datadir}/common-lisp

%find_lang %{name}

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING COPYING.LIB AUTHORS README NEWS ChangeLog
%{_bindir}/gpg-error
%{_libdir}/libgpg-error.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/gpg-error-config
%{_libdir}/libgpg-error.so
%{_includedir}/gpg-error.h
%{_datadir}/aclocal/gpg-error.m4
%{_libdir}/pkgconfig/*.pc

