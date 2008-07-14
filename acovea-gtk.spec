Summary:	A GTK-based User Interface for Acovea
Name:		acovea-gtk
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	bc659538b0b111715ddf0935ee775b6e
URL:		http://www.coyotegulch.com/products/acovea/acovea-gtk.html
BuildRequires:  gtkmm24-devel
BuildRequires:  libacovea-devel
BuildRequires:  libcoyotl-devel
BuildRequires:  libevocosm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Acovea engine ships with a command-line driver named runacovea. I
like command-line utilities, and probably spend as much time at the
prompt as I do clicking buttons. Still, a graphical interface can
provide a certain ease-of-use that is lacking in a command-line
application.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*.png
