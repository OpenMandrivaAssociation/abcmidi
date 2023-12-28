Summary:	Tool for processing ABC music notation files
Name:		abcmidi
Version:	2023.12.23
Release:	1
Source0:	https://ifdo.ca/~seymour/runabc/abcMIDI-%{version}.zip
Group:		Sound
License:	GPL
URL:		https://ifdo.ca/~seymour/runabc/top.html

%description
The abcMIDI package contains four programs: abc2midi to convert ABC music
notation to midi, midi2abc to convert midi files to (a first approximation
to) the corresponding ABC, abc2abc to reformat and/or transpose ABC files,
and yaps to typeset ABC files as PostScript.

For a description of the abc syntax, please see the abc userguide 
which is a part of the abc2mtex package written by Chris Walshaw.

%prep
%autosetup -p1 -n %{name}
rm -f configure makefile || die
sed -i -e "s:-O2::" configure.ac || die
autoreconf -fi
%configure

%build
%make_build

%install
%make_install

%files
%doc %{_defaultdocdir}/*
%{_mandir}/man1/*.1*
%{_bindir}/*
