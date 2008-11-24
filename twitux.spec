Name:           twitux
Version:        0.62
Release:        %mkrel 1
Summary:        Twitux is a Twitter client for the Gnome desktop
Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://sourceforge.net/projects/twitux/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	gnome-keyring-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libsexy-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libsoup-devel >= 2.3.4
BuildRequires:	libnotify-devel
BuildRequires:	glib2-devel >= 2.15.5
BuildRequires:	aspell-devel
BuildRequires:  gettext
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils

%description
Twitux is a Twitter client for the Gnome desktop.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %buildroot

%preun
%preun_uninstall_gconf_schemas twitux

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/twitux.*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
