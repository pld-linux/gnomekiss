# NOTE: version 2.0 for GNOME 2 available
Summary:	Implementation of French-KiSS for GNOME
Summary(pl.UTF-8):	Implementacja French-KiSS dla GNOME
Name:		gnomekiss
Version:	1.6
Release:	6
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.ecs.soton.ac.uk/~njl98r/code/kiss/%{name}-%{version}.tar.gz
# Source0-md5:	1b25fdb9c9e2959cd9f31c7550a8b0fa
Patch0:		%{name}-desktop.patch
URL:		http://www.ecs.soton.ac.uk/~njl98r/code/kiss/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeKiss is an implementation of French-KiSS for the GNOME desktop
environment, using GNOME, GTK+ and the X Window System. French KiSS is
an enhanced KiSS/GS for scriptable dolls, where KiSS is an
abbreviation for Kisekae Set System (or something).

%description -l pl.UTF-8
GnomeKiss jest implementacją French-KiSS dla desktopu GNOME.
Wykorzystuje GNOME, GTK+ i środowisko X Window. French KiSS jest
rozszerzonym KiSS/GS do oskryptowanych lalek, podczas gdy KiSS jest
implementacją Kissekae Set System (czy jakoś tak).

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicates es
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/es_ES
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*
