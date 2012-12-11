Name:           twitux
Version:        0.69
Release:        %mkrel 6
Summary:        Twitter client for the Gnome desktop
Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://sourceforge.net/projects/twitux/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		twitux-0.69-libnotify-0.7.patch
BuildRequires:	libgnome-keyring-devel
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.61
BuildRequires:	libsexy-devel
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	libsoup-devel >= 2.3.4
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(glib-2.0) >= 2.15.5
BuildRequires:	enchant-devel
BuildRequires:	pkgconfig(libcanberra-gtk) >= 0.4
BuildRequires:  gettext
BuildRequires:  rarian
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.3.2
BuildRequires:	intltool >= 0.35.0

%description
Twitux is a Twitter client for the Gnome desktop.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-schemas-install
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%preun
%preun_uninstall_gconf_schemas twitux

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/twitux.*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
