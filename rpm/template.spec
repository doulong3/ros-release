Name:           ros-indigo-roscreate
Version:        1.11.7
Release:        0%{?dist}
Summary:        ROS roscreate package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscreate
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
BuildRequires:  ros-indigo-catkin >= 0.5.68

%description
roscreate contains a tool that assists in the creation of ROS filesystem
resources. It provides: roscreate-pkg, which creates a new package directory,
including the appropriate build and manifest files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.7-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.6-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

