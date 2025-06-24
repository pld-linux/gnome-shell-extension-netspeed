Summary:	A gnome-shell extension to show speed of the internet
Name:		gnome-shell-extension-netspeed
Version:	48
Release:	1
License:	GPL v2+
Source0:	%{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	54ae25127a96d8b780674099a794ec1e
URL:		https://github.com/martinkg/NetSpeed
BuildRequires:	gettext
BuildRequires:	glib2
BuildRequires:	jq
BuildRequires:	meson
BuildRequires:	rpmbuild(macros) >= 1.726
BuildArch:	noarch

%define extuuid netspeed@hedayaty.gmail.com

%description
Add an Internet speed indicator to status area.

%prep
%setup -q -n NetSpeed-%{version}

%build
%meson \
	-Dlocal_install=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%{__rm} $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/gschemas.compiled

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%{_datadir}/gnome-shell/extensions/%{extuuid}
%{_datadir}/glib-2.0/schemas/*.gschema.xml
