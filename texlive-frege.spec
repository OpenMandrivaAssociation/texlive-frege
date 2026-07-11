%global tl_name frege
%global tl_revision 27417

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Typeset fregean Begriffsschrift
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/frege
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frege.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frege.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a number of new commands for typesetting fregean
Begriffsschrift in LaTeX. It is loosely based on the package begriff,
and offers a number of improvements including better relative lengths of
the content stroke with respect to other strokes, content strokes that
point at the middle of lines rather than the bottom, a greater width for
the assertion stroke as compared to the content stroke, a more intuitive
structure for the conditional, greater care taken to allow for the
linewidth in the spacing of formulas.

