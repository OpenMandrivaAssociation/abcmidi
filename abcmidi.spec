Summary:	Tool for processing ABC music notation files
Name:	abcmidi
Version:	2025.06.27
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://ifdo.ca/~seymour/runabc/top.html
# See also: https://sourceforge.net/projects/abcmidi/files/abcMIDI-%%{version}.zip
Source0:	https://github.com/sshlien/abcmidi/archive/refs/tags/%{name}-%{version}.tar.gz
# Avoid automatic install of docs: we take them with our %%doc macro
Patch0:	abcmidi-2025.06.27-dont-install-docs.patch

%description
The abcMIDI package contains four programs: abc2midi to convert ABC music
notation to midi, midi2abc to convert midi files to (a first approximation
to) the corresponding ABC, abc2abc to reformat and/or transpose ABC files,
and yaps to typeset ABC files as PostScript.

%files
%doc README.md doc/AUTHORS doc/CHANGES doc/abcguide.txt doc/history.txt doc/readme.txt
%{_bindir}/*
%{_mandir}/man1/*.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
rm -f configure makefile || die
sed -i -e "s:-O2::" configure.ac || die
autoreconf -vfi
%configure

%make_build


%install
%make_install
