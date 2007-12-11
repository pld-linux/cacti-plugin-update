%define		namesrc	update
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Update
Summary(pl.UTF-8):	Wtyczka do Cacti - Update
Name:		cacti-plugin-update
Version:	0.4
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins//%{namesrc}-%{version}.zip
# Source0-md5:	e594f4fd5ac9d35faac5fa5cdebe043e
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
It's an "administrative" plugin to help you keep track of all your
plugin versions. It will also check for Updates to Cacti, the Plugin
Architecture, and your Plugins and will alert you when it finds new
versions.

%description -l pl.UTF-8
To jest wtyczka "administracyjna" pomagająca śledzić wersje wszystkich
posiadanych wtyczek. Ponadto sprawdza uaktualnienia do Cacti,
architektury wtyczek oraz samych wtyczek i ostrzega, kiedy znajdzie
nowe wersje.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
