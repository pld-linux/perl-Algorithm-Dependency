#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		pdir	Algorithm
%define		pnam	Dependency
Summary:	Algorithm::Dependency - Base class for implementing various dependency trees
Summary(pl.UTF-8):	Algorithm::Dependency - podstawowa klasa do tworzenia różnych drzew zależności
Name:		perl-Algorithm-Dependency
Version:	1.112
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d848624b0c483adf7f7f60f6ae2edc8f
URL:		https://metacpan.org/release/Algorithm-Dependency
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Params-Util >= 0.31
BuildRequires:	perl-Scalar-List-Utils >= 1.11
BuildRequires:	perl-Test-ClassAPI >= 0.6
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base class for implementing various dependency trees.

%description -l pl.UTF-8
Podstawowa klasa do tworzenia różnych drzew zależności.

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
