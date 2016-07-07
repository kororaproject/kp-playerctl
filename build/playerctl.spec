Name:           playerctl
Version:        0.5.0
Release:        1%{?dist}.1
Summary:        Command-line utility and library for controlling media players

License:        GPLv3
URL:            https://github.com/acrisci/playerctl
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gobject-introspection-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc

%description
Playerctl is a command-line utility and library for controlling media players that implement the MPRIS D-Bus Interface Specification. Playerctl makes it easy to bind player actions, such as play and pause, to media keys.

%prep
%setup -q


%build

./autogen.sh --prefix=%{_prefix} --libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README.md
%{_bindir}/playerctl
%{_libdir}/libplayerctl*
%{_libdir}/girepository-1.0/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%{_includedir}/playerctl/*

%changelog
* Mon Jul 04 2016 Matthew Oliver - 0.5.0-1
- Initial release
