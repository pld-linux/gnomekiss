Summary:	Implementation of French-KiSS for GNOME
Summary(pl):	Implementacja French-KiSS dla GNOME
Name:		gnomekiss
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.ecs.soton.ac.uk/~njl98r/code/kiss/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
GnomeKiss is an implementation of French-KiSS for the GNOME desktop
environment, using GNOME, GTK+ and the X Window System. French KiSS is
an enhanced KiSS/GS for scriptable dolls, where KiSS is an
abbreviation for Kisekae Set System (or something).

%description -l pl
GnomeKiss jest implementacj± French-KiSS dla desktopu GNOME.
Wykorzystuje GNOME, GTK+ i ¶rodowisko X Window. French KiSS jest
rozszerzonym KiSS/GS do oskryptowanych lalek, podczas gdy KiSS jest
implementacj± Kissekae Set System (czy jako¶ tak).

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
