Name:		texlive-frege
Version:	27417
Release:	1
Summary:	Typeset fregean Begriffsschrift
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frege
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frege.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frege.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a number of new commands for typesetting
fregean Begriffsschrift in LaTeX. It is loosely based on the
package begriff, and offers a number of improvements including
better relative lengths of the content stroke with respect to
other strokes, content strokes that point at the middle of
lines rather than the bottom, a greater width for the assertion
stroke as compared to the content stroke, a more intuitive
structure for the conditional, greater care taken to allow for
the linewidth in the spacing of formulas.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frege/frege.sty
%doc %{_texmfdistdir}/doc/latex/frege/GNU.txt
%doc %{_texmfdistdir}/doc/latex/frege/INSTALL
%doc %{_texmfdistdir}/doc/latex/frege/README
%doc %{_texmfdistdir}/doc/latex/frege/frege.pdf
%doc %{_texmfdistdir}/doc/latex/frege/frege.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
