#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Unit
Summary:	Test::Unit Perl module
Summary(cs.UTF-8):	Modul Test::Unit pro Perl
Summary(da.UTF-8):	Perlmodul Test::Unit
Summary(de.UTF-8):	Test::Unit Perl Modul
Summary(es.UTF-8):	Módulo de Perl Test::Unit
Summary(fr.UTF-8):	Module Perl Test::Unit
Summary(it.UTF-8):	Modulo di Perl Test::Unit
Summary(ja.UTF-8):	Test::Unit Perl モジュール
Summary(ko.UTF-8):	Test::Unit 펄 모줄
Summary(nb.UTF-8):	Perlmodul Test::Unit
Summary(pl.UTF-8):	Moduł Perla Test::Unit
Summary(pt.UTF-8):	Módulo de Perl Test::Unit
Summary(pt_BR.UTF-8):	Módulo Perl Test::Unit
Summary(ru.UTF-8):	Модуль для Perl Test::Unit
Summary(sv.UTF-8):	Test::Unit Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Test::Unit
Summary(zh_CN.UTF-8):	Test::Unit Perl 模块
Name:		perl-Test-Unit
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bbd92a461996ae978ac378eae477bd79
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
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

%description -l pl.UTF-8
Ten pakiet udostępnia szkielet do obsługi testów poszczególnych części
obiektowo zorientowanej aplikacji (z obsługą dziedziczenia testów, itp.).

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
%{_examplesdir}/%{name}-%{version}/fail_example.pm
%{_examplesdir}/%{name}-%{version}/tester.png
%{_examplesdir}/%{name}-%{version}/[RE]*
