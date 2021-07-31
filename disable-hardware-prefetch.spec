Name:   disable-hardware-prefetch
Version:    0.1 
Release:    1%{?dist}
Summary:    Disable hardware prefetch on Intel CPU
License:    GPL
URL:	    https://github.com/pjakma/disable-hardware-prefetch
Source:    disable-hardware-prefetch-%{version}.tar.gz


%description
Disable hardware prefetchers on Intel CPU, via model specific registers.
See:
https://software.intel.com/content/www/us/en/develop/articles/disclosure-of-hw-prefetcher-control-on-some-intel-processors.html

Older Core and NetBurst:
https://software.intel.com/content/www/us/en/develop/articles/optimizing-application-performance-on-intel-coret-microarchitecture-using-hardware-implemented-prefetchers.html

%global debug_package %{nil}

%prep
%setup -q


%build


%install
install --directory $RPM_BUILD_ROOT%{_sbindir}
install --directory $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 disable-hardware-prefetch.service $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0755 disable-hardware-prefetch.sh $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_sbindir}/disable-hardware-prefetch.sh
%{_unitdir}/disable-hardware-prefetch.service

%changelog
