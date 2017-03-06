Name:           ros-jade-roslib
Version:        1.12.8
Release:        0%{?dist}
Summary:        ROS roslib package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslib
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg >= 1.0.37
Requires:       ros-jade-catkin
Requires:       ros-jade-rospack
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin >= 0.6.7
BuildRequires:  ros-jade-rospack

%description
Base dependencies and support libraries for ROS. roslib contains many of the
common data structures and tools that are shared across ROS client library
implementations.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Mar 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

* Thu Apr 21 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.7-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.6-0
- Autogenerated by Bloom

* Tue Oct 13 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Mon Oct 12 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

* Sat Sep 19 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.3-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.1-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

