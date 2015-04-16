Name:           ros-jade-mk
Version:        1.12.1
Release:        0%{?dist}
Summary:        ROS mk package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-rosbuild
BuildRequires:  ros-jade-catkin >= 0.5.69

%description
A collection of .mk include files for building ROS architectural elements. Most
package authors should use cmake .mk, which calls CMake for the build of the
package. The other files in this package are intended for use in exotic
situations that mostly arise when importing 3rdparty code.

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
* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.1-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

