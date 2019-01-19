Name:          sailfishos-patch-silicamail
Version:       0.1
Release:       5
Summary:       Silica Mail
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 3.0.1, patchmanager
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Tweaks for the Jolla e-mail client.

%files
%defattr(-,root,root,-)
/usr/share/*

%preun
patchmanager -u sailfishos-patch-silicamail

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
	rm -rf /usr/share/patchmanager/patches/sailfishos-patch-silicamail

else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
        patchmanager -u sailfishos-patch-silicamail
fi
fi

%changelog
* Sat Jan 19 2019 0.1
- First build.
