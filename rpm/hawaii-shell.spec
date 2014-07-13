# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       hawaii-shell

# >> macros
# << macros

Summary:    Hawaii user interface for desktop and mobile
Version:    0.2.99
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1+ and GPLv2+
URL:        https://github.com/mauios/hawaii-shell.git
Source0:    %{name}-%{version}.tar.xz
Source100:  hawaii-shell.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  kf5-rpm-macros
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-plasma-devel

%description
Provides Hawaii desktop environment shell.


%package -n hawaii-desktop-session
Summary:    Hawaii desktop session
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   hawaii-desktop-shell
Conflicts:  kde5-plasma-workspace-shell

%description -n hawaii-desktop-session
This package contains the files that bring up the Hawaii |
desktop shell.


%package -n hawaii-desktop-shell
Summary:    Hawaii desktop shell
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   qt5-qtdeclarative-import-window2
Requires:   qt5-qtsvg-plugin-imageformat-svg
Requires:   qt5-qttools-qdbus
Requires:   qt5-qtquickcontrols
Requires:   qt5-qtgraphicaleffects
Requires:   dbus-x11
Requires:   accountsservice
Requires:   sddm
Requires:   kde5-plasma-desktop
Requires:   kde5-plasma-workspace
Requires:   kde5-plasma-workspace-plasmoids
Requires:   kde5-plasma-workspace-wallpapers

%description -n hawaii-desktop-shell
This package contains the files necessary to run the |
Hawaii desktop shell.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
# << install post


%files -n hawaii-desktop-session
%defattr(-,root,root,-)
%{_datadir}/xsessions/hawaii.desktop
%{_datadir}/wayland-sessions/hawaii.desktop
%{_kde5_sysconfdir}/xdg/autostart/hawaii-shell-desktop.desktop
%{_libdir}/systemd/user/*
# >> files hawaii-desktop-session
# << files hawaii-desktop-session

%files -n hawaii-desktop-shell
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB README.md
%{_kde5_datadir}/plasma/look-and-feel/org.hawaii.lookandfeel.desktop/*
%{_kde5_datadir}/plasma/shells/org.hawaii.shells.desktop/*
%{_datadir}/sddm/themes/mauiproject/*
# >> files hawaii-desktop-shell
# << files hawaii-desktop-shell
