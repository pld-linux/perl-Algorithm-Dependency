#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	Dependency
Summary:	Algorithm::Dependency - Base class for implementing various dependency trees
Summary(pl.UTF-8):	Algorithm::Dependency - Podstawowa klasa do tworzenia różnych drzewek zależności
Name:		perl-Algorithm-Dependency
Version:	1.104
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88a0a0214b44d49a0dfcb8bd070aaf4f
%if %{with tests}
BuildRequires:	perl-Config-Tiny
BuildRequires:	perl-Params-Util
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base class for implementing various dependency trees

%description -l pl.UTF-8
Podstawowa klasa do tworzenia różnych drzewek zależności

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Algorithm/*.pm
%{perl_vendorlib}/Algorithm/Dependency
%{_mandir}/man3/*
