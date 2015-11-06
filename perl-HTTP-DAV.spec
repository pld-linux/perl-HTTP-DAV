#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	DAV
%include	/usr/lib/rpm/macros.perl
Summary:	HTTP::DAV - A WebDAV client library for Perl5
Summary(pl.UTF-8):	HTTP::DAV - biblioteka kliencka WebDAV dla Perla 5
Name:		perl-HTTP-DAV
Version:	0.48
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d58cccad5eab48782548958f71c2f0e1
URL:		http://search.cpan.org/dist/HTTP-DAV/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP::DAV is a Perl API for interacting with and modifying content on
webservers using the WebDAV protocol. Now you can LOCK, DELETE and PUT
files and much more on a DAV-enabled webserver.

%description -l pl.UTF-8
HTTP::DAV jest perlowym API przeznaczonym do współpracy z serwerami
webowymi z wykorzystaniem protokołu WebDAV. Można korzystać z
operacji LOCK, DELETE i PUT oraz wielu innych udostępnianych przez
serwer.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{_bindir}/dave
%{perl_vendorlib}/HTTP/DAV.pm
%{perl_vendorlib}/HTTP/DAV
%{_mandir}/man1/dave.*
%{_mandir}/man3/HTTP::DAV*
