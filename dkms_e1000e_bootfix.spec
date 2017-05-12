Name:           dkms_e1000e_bootfix
Version:        4.10.14.patch1
Release:        1%{?dist}
Summary:        DKMS package applying fixes to Intel e1000e kernel module
Group:          System Environment/Kernel
License:        GPLv2
URL:            https://github.com/jwmullally/dkms_e1000e_bootfix
Requires:       dkms
Requires(post): dkms
Requires(preun): dkms
BuildArch:      noarch
Source0:        %{name}-%{version}.tgz

%description
DKMS package applying fixes to Intel e1000e kernel module.

Applies patch https://patchwork.kernel.org/patch/9254367/ to
Linux kernel v4.10.14 e1000e module to workaround 
"e1000e: probe of 0000:00:19.0 failed with error -3"
errors on cold boot of Intel 82578DC Gigabit Ethernet PHY for some 
affected hardware/BIOS configurations.

%prep
%setup -q

%install
DKMS_DIR=%{buildroot}/usr/src/%{name}-%{version}/
install -m 755 -d $DKMS_DIR
install -m 644 dkms.conf $DKMS_DIR/
install -m 755 -d $DKMS_DIR/e1000e
install -m 644 -t $DKMS_DIR/e1000e e1000e/*
install -m 755 -d $DKMS_DIR/patches
install -m 644 -t $DKMS_DIR/patches patches/*

%post
dkms add     -m %{name} -v %{version} --rpm_safe_upgrade &&
dkms build   -m %{name} -v %{version} --rpm_safe_upgrade &&
dkms install -m %{name} -v %{version} --rpm_safe_upgrade --force
true

%preun
dkms remove  -m %{name} -v %{version} --rpm_safe_upgrade --all
true

%files
/usr/src/%{name}-%{version}/

%changelog
* Fri May 12 2017 Joseph Mullally <jwmullally@gmail.com>
- Initial package
