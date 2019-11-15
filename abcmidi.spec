Summary:	Tool for processing ABC music notation files
Name:		abcmidi
Version:	2019.07.12
Release:	1
Source0:	http://ifdo.pugmarks.com/~seymour/runabc/abcMIDI-2012-07-04.zip
Group:		Sound
License:	GPL
URL:		http://ifdo.ca/welcome_e.asp
#Patch0:		abcmidi-2011.10.19-install.patch


%description
The abcMIDI package contains four programs: abc2midi to convert ABC music
notation to midi, midi2abc to convert midi files to (a first approximation
to) the corresponding ABC, abc2abc to reformat and/or transpose ABC files,
and yaps to typeset ABC files as PostScript.

For a description of the abc syntax, please see the abc userguide 
which is a part of the abc2mtex package written by Chris Walshaw.

%prep
%setup -q -n %{name}
#patch0 -p1


%build
rm configure makefile || die
sed -i -e "s:-O2::" configure.ac || die
autoreconf -fi
%configure
%make

%install
%makeinstall_std

%files
%doc doc/CHANGES VERSION
%doc %{_mandir}/man1/*
%{_bindir}/*


