Summary: PuppetLabs Stdlib Module
Name: puppetlabs-stdlib
Version: 4.9.0
Release: 0.SIMP
License: Apache License, 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet >= 3.3.2
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0

Prefix: %{_sysconfdir}/puppet/environments/simp/modules

%description
This is the puppetlabs stdlib module as hosted at
https://github.com/puppetlabs/puppetlabs-stdlib.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/stdlib

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/stdlib
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/stdlib

%files
%defattr(0640,root,puppet,0750)
%{prefix}/stdlib

%post
#!/bin/sh

%postun
# Post uninstall stuff

%changelog
* Mon Nov 17 2016 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.9.0-0.SIMP
- Patching in the latest official 4.9.0

* Mon Feb 02 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.5.1-0.SIMP
- Patching in the latest official 4.5.1

* Mon Apr 14 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-1.SIMP
- Patching in the latest official 4.1.0

* Mon Apr 07 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-0.SIMP
- Fixed issues with string handling in join
- Fixed issues with non-string handling in is_integer

* Mon Dec 16 2013 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-0
- Incorporated and packaged from the remote repository.
- Commit: 1ffd72daaaf21e71e762b6cd543043680bdb6694
- Rakefile and spec file added to make RPM builds easier.
