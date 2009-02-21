%define base_name	creal
%define name		ocaml-%{base_name}
%define version		0.7
%define release		%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Exact real arithmetic for Objective Caml
URL:		http://www.lri.fr/~filliatr/software.en.html
Source0:	http://www.lri.fr/~filliatr/ftp/ocaml/ds/%{base_name}-%{version}.tar.bz2
Source1:	ocaml-cairo-META
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  gmp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Creal is an exact real arithmetic library for Objective Caml.	
This  module  implements  exact  real  arithmetic,  following  Valérie
Ménissier-Morain Ph.D. thesis (http://www-calfor.lip6.fr/~vmm/).
A  real  x  is  represented  as  a function  giving,  for  any  n,  an
approximation zn/4^n of x  such that |zn/4^n - x| < 1,  where zn is an
arbitrary precision integer (of type Gmp.Z.t).
Coercions from type int, Gmp.Z.t, Gmp.Q.t, basic operations (addition,
subtraction,  multiplication,   division,  power,  square   root)  and
transcendental  functions (sin,  cos, tan,  log, exp,  arcsin, arccos,
etc.) and a few constants (pi, e) are provided.
A small reverse-polish calculator is provided to test the library.
Written by Jean-Christophe Filliâtre.

%package devel
Summary:	Exact real arithmetic for Objective Caml
Group:		Development/Other
Requires:   gmp-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Creal is an exact real arithmetic library for Objective Caml.	

%prep
%setup -q -n %{base_name}-%{version}
chmod 644 README CHANGES *.mli mlgmp/*.mli
perl -pi -e 's/\015$//' README
# TODO: gmp.cma  gmp.cmxa (pp)
cp %{SOURCE1} META

%build
%configure
%make
sed -i -e 's:@VERSION@:%{version}:g' META

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}/ocaml/%{base_name}
make LIBDIR=%{buildroot}%{_libdir}/ocaml/%{base_name} install-lib

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%dir %{_libdir}/ocaml/creal
%{_libdir}/ocaml/creal/*.cmi
%{_libdir}/ocaml/creal/*.cma

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/creal/*.a
%{_libdir}/ocaml/creal/*.cmxa
%{_libdir}/ocaml/creal/*.mli
