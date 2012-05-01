%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:      mingw32-gettext
Version:   0.17
Release:   12%{?dist}.4
Summary:   GNU libraries and utilities for producing multi-lingual messages


License:   GPLv2+ and LGPLv2+
Group:     Development/Libraries
URL:       http://www.gnu.org/software/gettext/
Source0:   http://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:    mingw32-gettext-0.17-gnulib-optarg-symbols.patch

BuildArch: noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires: mingw32-runtime >= 3.15.1
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-iconv
BuildRequires: mingw32-termcap >= 1.3.1-3

# Possible extra BRs.  These are used if available, but
# not required just for building.
#BuildRequires: mingw32-dlfcn
#BuildRequires: mingw32-libxml2
#BuildRequires: mingw32-expat
#BuildRequires: mingw32-glib2


%description
MinGW Windows Gettext library


%package static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the MinGW Windows Gettext library.


%prep
%setup -q -n gettext-%{version}

%patch0 -p1


%build
%{_mingw32_configure} \
  --disable-java \
  --disable-native-java \
  --disable-csharp \
  --enable-static \
  --enable-threads=win32 \
  --without-emacs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_mingw32_datadir}/locale/locale.alias
rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{_mingw32_datadir}/info/dir

# Remove man pages, these are available in base gettext-devel.
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}/man1/
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}/man3/

%find_lang %{name} --all-name


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_mingw32_bindir}/autopoint
%{_mingw32_bindir}/envsubst.exe
%{_mingw32_bindir}/gettext.exe
%{_mingw32_bindir}/gettext.sh
%{_mingw32_bindir}/gettextize
%{_mingw32_bindir}/libasprintf-0.dll
%{_mingw32_bindir}/libgettextlib-0-17.dll
%{_mingw32_bindir}/libgettextpo-0.dll
%{_mingw32_bindir}/libgettextsrc-0-17.dll
%{_mingw32_bindir}/libintl-8.dll
%{_mingw32_bindir}/msg*.exe
%{_mingw32_bindir}/ngettext.exe
%{_mingw32_bindir}/recode-sr-latin.exe
%{_mingw32_bindir}/xgettext.exe

%{_mingw32_includedir}/autosprintf.h
%{_mingw32_includedir}/gettext-po.h
%{_mingw32_includedir}/libintl.h

%{_mingw32_libdir}/gettext

%{_mingw32_libdir}/libasprintf.dll.a
%{_mingw32_libdir}/libasprintf.la

%{_mingw32_libdir}/libgettextlib.dll.a
%{_mingw32_libdir}/libgettextlib.la

%{_mingw32_libdir}/libgettextpo.dll.a
%{_mingw32_libdir}/libgettextpo.la

%{_mingw32_libdir}/libgettextsrc.dll.a
%{_mingw32_libdir}/libgettextsrc.la

%{_mingw32_libdir}/libintl.dll.a
%{_mingw32_libdir}/libintl.la

%{_mingw32_docdir}/gettext
%{_mingw32_docdir}/libasprintf/autosprintf_all.html

%{_mingw32_datadir}/gettext/

%{_mingw32_datadir}/aclocal/*m4
%{_mingw32_datadir}/info/autosprintf.info
%{_mingw32_datadir}/info/gettext.info

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libasprintf.a
%{_mingw32_libdir}/libgettextpo.a
%{_mingw32_libdir}/libintl.a


%changelog
* Mon Dec 27 2010 Andrew Beekhof <abeekhof@redhat.com> - 0.17-12.4
- Rebuild everything with gcc-4.4
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 0.17-12.3
- The use of ExclusiveArch conflicts with noarch, using an alternate COLLECTION to limit builds
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 0.17-12.2
- Only build mingw packages on x86_64
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 0.17-12.1
- Bump the revision to avoid tag collision
  Related: rhbz#658833

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.17-11
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-9
- Rebuild for mingw32-gcc 4.4

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-8
- Use find_lang macro.

* Fri Jan 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-7
- Remove the manpages - already available in base Fedora gettext-devel.
- Use _smp_mflags for build.
- Added list of potential BRs.
- Added license file to doc section.

* Fri Oct 31 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-6
- Add fix for undefined Gnulib symbols (Farkas Levente).
- Rebuild against mingw32-termcap / libtermcap.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-5
- Rename mingw -> mingw32.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 0.17-4
- Disable emacs lisp file install

* Thu Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-3
- Remove static libraries.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-2
- Use RPM macros from mingw-filesystem.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 0.17-1
- Initial RPM release, largely based on earlier work from several sources.
