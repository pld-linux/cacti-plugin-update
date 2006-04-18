%define		namesrc	update
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Update
Summary(pl):	Wtyczka do Cacti - Update
Name:		cacti-plugin-update
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	02ca51dee355d671cf61a4421bb7f69c
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
versions. Currently it does not import its own table, so you will have
to do that yourself. I should have that issue fixed in the next
version.

%description -l pl
To jest wtyczka "administracyjna" pomagaj±ca ¶ledziæ wersje wszystkich
posiadanych wtyczek. Ponadto sprawdza uaktualnienia do Cacti,
architektury wtyczek oraz samych wtyczek i ostrzega, kiedy znajdzie
nowe wersje. Aktualnie nie obs³uguje w³asnej tabeli, wiêc trzeba j±
zrobiæ samemu. Powinno to byæ poprawione w nastêpnej wersji.

%prep
%setup -q -n %{namesrc}

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
