Name:           playerctl
Version:        0.5.0 
Release:        1%{?dist}
Summary:        Command-line utility and library for controlling media players

License:        GPLv3
URL:            https://github.com/acrisci/playerctl
Source0:        https://github.com/acrisci/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gobject-introspection-devel
BuildRequires:  glib2-devel
#BuildRequires:  
#Requires:       

%description
Playerctl is a command-line utility and library for controlling media players that implement the MPRIS D-Bus Interface Specification. Playerctl makes it easy to bind player actions, such as play and pause, to media keys.

%prep
%setup -q


%build
./autogen.sh --prefix=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README.md
%{_bindir}/playerctl
%{_prefix}/lib/libplayerctl*
%{_prefix}/lib/girepository-1.0/*
%{_prefix}/lib/pkgconfig/*
/usr/share/gir-1.0/*
/usr/include/playerctl/*

%changelog
* Mon Jul  4 2016 Matthew Oliver
- 
