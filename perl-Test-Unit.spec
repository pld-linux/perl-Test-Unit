%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Unit
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	0.24
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This framework is intended to support unit testing in an object-oriented
development paradigm (with support for inheritance of tests etc.) and
is derived from the JUnit testing framework for Java by Kent Beck and
Erich Gamma.

%description -l pl
Ten pakiet udostêpnia szkielet do obs³ugi testów poszczególnych czê¶ci
obiektowo zorientowanej aplikacji (z obs³ug± dziedziczenia testów, etc.).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf examples/README
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* AUTHORS
%{perl_sitelib}/%{pdir}/*.pl
%{perl_sitelib}/%{pdir}/*.pm
%dir %{perl_sitelib}/%{pdir}/%{pnam}
%{perl_sitelib}/%{pdir}/%{pnam}/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
