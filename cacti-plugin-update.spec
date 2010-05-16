%define		plugin	update
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Update
Summary(pl.UTF-8):	Wtyczka do Cacti - Update
Name:		cacti-plugin-update
Version:	0.4
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins//%{plugin}-%{version}.zip
# Source0-md5:	e594f4fd5ac9d35faac5fa5cdebe043e
Patch0:		%{name}-adodb.patch
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
