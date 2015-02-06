%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define modname creal

Summary:	Exact real arithmetic for Objective Caml
Name:		ocaml-%{modname}
Version:	0.7
Release:	10
License:	LGPLv2+
Group:		Development/Other
Url:		http://www.lri.fr/~filliatr/software.en.html
Source0:	http://www.lri.fr/~filliatr/ftp/ocaml/ds/%{modname}-%{version}.tar.bz2
Source1:	ocaml-creal-META
BuildRequires:	ocaml
BuildRequires:	gmp-devel

%description
Creal is an exact real arithmetic library for Objective Caml.

This module implements exact real arithmetic, following Valerie
Menissier-Morain Ph.D. thesis (http://www-calfor.lip6.fr/~vmm/).

A real x is represented as a function giving, for any n, an
approximation zn/4^n of x such that |zn/4^n - x| < 1, where zn is an
arbitrary precision integer (of type Gmp.Z.t).

Coercions from type int, Gmp.Z.t, Gmp.Q.t, basic operations (addition,
subtraction, multiplication, division, power, square root) and
transcendental functions (sin, cos, tan, log, exp, arcsin, arccos,
etc.) and a few constants (pi, e) are provided.

A small reverse-polish calculator is provided to test the library.

%files
%doc README CHANGES
%dir %{_libdir}/ocaml/creal
%{_libdir}/ocaml/creal/*.cmi
%{_libdir}/ocaml/creal/*.cma

#----------------------------------------------------------------------------

%package devel
Summary:	Exact real arithmetic for Objective Caml
Group:		Development/Other
Requires:	gmp-devel
Requires:	%{name} = %{EVRD}

%description devel
Creal is an exact real arithmetic library for Objective Caml.

%files devel
%{_libdir}/ocaml/creal/*.a
%{_libdir}/ocaml/creal/*.cmxa
%{_libdir}/ocaml/creal/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n %{modname}-%{version}
chmod 644 README CHANGES *.mli mlgmp/*.mli
perl -pi -e 's/\015$//' README
# TODO: gmp.cma gmp.cmxa (pp)
cp %{SOURCE1} META

%build
%configure
%make
sed -i -e 's:@VERSION@:%{version}:g' META

%install
install -d %{buildroot}%{_libdir}/ocaml/%{modname}
make LIBDIR=%{buildroot}%{_libdir}/ocaml/%{modname} install-lib

