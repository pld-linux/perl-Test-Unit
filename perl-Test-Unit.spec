#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Unit
Summary:	Test::Unit Perl module
Summary(cs):	Modul Test::Unit pro Perl
Summary(da):	Perlmodul Test::Unit
Summary(de):	Test::Unit Perl Modul
Summary(es):	Módulo de Perl Test::Unit
Summary(fr):	Module Perl Test::Unit
Summary(it):	Modulo di Perl Test::Unit
Summary(ja):	Test::Unit Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Test::Unit ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Test::Unit
Summary(pl):	Modu³ Perla Test::Unit
Summary(pt):	Módulo de Perl Test::Unit
Summary(pt_BR):	Módulo Perl Test::Unit
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Test::Unit
Summary(sv):	Test::Unit Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Test::Unit
Summary(zh_CN):	Test::Unit Perl Ä£¿é
Name:		perl-%{pdir}-%{pnam}
Version:	0.24
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e05b5e2f0cd2d9537d63b7a9471eed5d
BuildRequires:	perl-devel >= 5
%if %{!?_without_tests:1}0
BuildRequires:	perl-Class-Inner
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-Error
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional (for Test::Unit::TkTestRunner only)
# (or maybe create subpackage with TkTestRunner?)
%define		_noautoreq	'perl(Tk.*)'

%description
This framework is intended to support unit testing in an object-oriented
development paradigm (with support for inheritance of tests etc.) and
is derived from the JUnit testing framework for Java by Kent Beck and
Erich Gamma.

%description -l pl
Ten pakiet udostêpnia szkielet do obs³ugi testów poszczególnych czê¶ci
obiektowo zorientowanej aplikacji (z obs³ug± dziedziczenia testów, itp.).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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
%attr(755,root,root) %{perl_vendorlib}/%{pdir}/*.pl
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}/*
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/p*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/tester.pl
%{_examplesdir}/%{name}-%{version}/tester.png
%{_examplesdir}/%{name}-%{version}/[RE]*
