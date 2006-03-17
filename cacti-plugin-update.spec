%define		namesrc	update
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Update
Summary(pl):	Wtyczka do Cacti - Update
Name:		cacti-plugin-update
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	0f4c0e881f35b3d6a23ea326f703d47d
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
its an "administrative" plugin to help you keep track of all your 
plugin versions. It will also check for Updates to Cacti, the Plugin 
Architecture, and your Plugins and will alert you when it finds new
versions. Currently it does not import its own table, so you will have
to do that yourself. I should have that issue fixed in the next version.

 %description -l pl
Wtyczka do Cacti - 

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
%doc CHANGES LICENSE README
%{webcactipluginroot}
