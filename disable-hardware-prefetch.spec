Name:   disable-hardware-prefetch
Version:    0.1.1
Release:    1%{?dist}
Summary:    Disable hardware prefetch on Intel CPU
License:    GPL
URL:        https://github.com/pjakma/disable-hardware-prefetch
Source:     disable-hardware-prefetch-%{version}.tar.gz

BuildRequires: systemd-rpm-macros
%{?systemd_requires}


%description
Disable hardware prefetchers on Intel CPU, via model specific registers.
See:
https://software.intel.com/content/www/us/en/develop/articles/disclosure-of-hw-prefetcher-control-on-some-intel-processors.html

Older Core and NetBurst:
https://software.intel.com/content/www/us/en/develop/articles/optimizing-application-performance-on-intel-coret-microarchitecture-using-hardware-implemented-prefetchers.html

%global debug_package %{nil}

%prep
%autosetup -p1

%build

%post
%systemd_post %{name}.service

        
%preun
%systemd_preun %{name}.service
 
%postun
%systemd_postun_with_restart %{name}.service

%install
install --directory $RPM_BUILD_ROOT%{_sbindir}
install --directory $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 disable-hardware-prefetch.service $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0755 disable-hardware-prefetch.sh $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_sbindir}/%{name}.sh
%{_unitdir}/%{name}.service

%changelog
* Mon Aug 02 2021 Paul Jakma <paul@jakma.org> 0.1.1-1
- Fedora Copr doesn't know _unitdir on Fedora for some reason, try fix.
  (paul@jakma.org)

* Mon Aug 02 2021 Paul Jakma <paul@jakma.org> 0.1-1
- new package built with tito

