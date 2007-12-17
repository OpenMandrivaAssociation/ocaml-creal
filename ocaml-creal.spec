%define base_name	creal
%define name		ocaml-%{base_name}
%define version		0.7
%define release		%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Exact real arithmetic for Objective Caml
Source: 	http://www.lri.fr/~filliatr/ftp/ocaml/ds/%{base_name}-%{version}.tar.bz2
URL:		http://www.lri.fr/~filliatr/software.en.html
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  gmp-devel

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

%build
%configure
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{ocaml_sitelib}/%{base_name}
make LIBDIR=%{buildroot}%{ocaml_sitelib}/%{base_name} install-lib

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%dir %{ocaml_sitelib}/creal
%{ocaml_sitelib}/creal/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/creal/*
%exclude %{ocaml_sitelib}/creal/*.cmi
