
%define	short_name	curve
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	LaTeX2e package for typesetting Curricula Vitae
Summary(pl.UTF-8):	Pakiet LaTeX2e do składania życiorysów (Curricula Vitae)
Name:		tetex-latex-%{short_name}
Version:	1.0.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	0d246701a2ccba0e073f5c18c3d51de2
BuildRequires:	tetex-format-latex
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-latex-carlisle
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CurVe is a class package that hopefully will make your life easier
when you want to write your CV. It provides you with a set of commands
to create rubrics, entries in these rubrics etc. CurVe will then
properly format your CV for you (possibly splitting it onto multiple
pages, repeating the titles etc), which is usually the most painful
part of CV writing. Another nice feature of CurVe is its ability to
manage different CV "flavors" simultaneously. It is in fact often the
case that you want to maintain slightly divergent versions of your CV
at the same time, in order to emphasize on different aspects of your
background.

%description -l pl.UTF-8
Klasa CurVe ma za zadanie ułatwiać życie podczas pisania życiorysów
(CV). Udostępnia zestaw komend do tworzenia rubryk i wpisów w nich.
CurVe może prawidłowo sformatować CV (rozdzielając je na kilka stron,
powtarzając tytuły itp), co jest męczącą częścią pisania CV. Kolejną
miłą właściwością CurVe jest łatwe zarządzanie kilkoma różnymi CV na
raz - co jest często wykorzystywane w sytuacji gdy należy używać kilku
różnych wersji CV w zależności od potrzeb.

%prep
%setup -q -n %{short_name}

%build
latex curve.ins
latex curve.dtx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.cls *.tex *.dvi $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README NEWS rubric.tex cv.tex
%{_datadir}/texmf/tex/latex/%{short_name}
