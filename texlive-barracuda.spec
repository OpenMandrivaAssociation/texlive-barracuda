Name:		texlive-barracuda
Version:	63708
Release:	2
Summary:	Draw barcodes with Lua
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/barracuda
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barracuda.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barracuda.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The barracuda library is a modular Lua package for drawing
barcode symbols. It provides modules for writing barcodes from
a LuaTeX document. It is also possible to use Barracuda with a
standalone Lua interpreter to draw barcodes in different
graphic formats like SVG.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/barracuda
%{_texmfdistdir}/scripts/barracuda
%doc %{_texmfdistdir}/doc/luatex/barracuda

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
