Summary:	abcMIDI is a package of programs developed by James Allwright for processing ABC music notation files
Name:		abcmidi
Version:	2011.11.18
Release:	1
Source0:	abcMIDI-2011-11-18.zip
Group:		Sound
License:	GPL
URL:		http://ifdo.pugmarks.com/~seymour/runabc/top.html

%description
The abcMIDI package contains four programs: abc2midi to convert ABC music
notation to midi, midi2abc to convert midi files to (a first approximation
to) the corresponding ABC, abc2abc to reformat and/or transpose ABC files,
and yaps to typeset ABC files as PostScript.

For a description of the abc syntax, please see the abc userguide 
which is a part of the abc2mtex package written by Chris Walshaw.

%prep
%setup -q -n %{name}

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 abc2midi %{buildroot}%{_bindir}
install -m 755 abcmatch %{buildroot}%{_bindir}
install -m 755 midi2abc %{buildroot}%{_bindir}
install -m 755 midicopy %{buildroot}%{_bindir}
install -m 755 abc2abc %{buildroot}%{_bindir}
install -m 755 mftext %{buildroot}%{_bindir}
install -m 755 yaps %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/abc2abc.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/abc2midi.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/mftext.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/midi2abc.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/midicopy.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/yaps.1 %{buildroot}%{_mandir}/man1

chmod 644 doc/*

%files
%doc doc/CHANGES VERSION
%doc %{_mandir}/*
%{_bindir}/*
