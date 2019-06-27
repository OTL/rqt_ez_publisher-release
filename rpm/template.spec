Name:           ros-melodic-rqt-ez-publisher
Version:        0.5.0
Release:        1%{?dist}
Summary:        ROS rqt_ez_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_ez_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rqt-gui
Requires:       ros-melodic-rqt-gui-py
Requires:       ros-melodic-rqt-py-common
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf2-msgs
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs

%description
The rqt_ez_publisher package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jun 27 2019 Takashi Ogura <t.ogura@gmail.com> - 0.5.0-1
- Autogenerated by Bloom

* Thu Jun 27 2019 Takashi Ogura <t.ogura@gmail.com> - 0.4.0-2
- Autogenerated by Bloom

* Tue Jun 25 2019 Takashi Ogura <t.ogura@gmail.com> - 0.4.0-1
- Autogenerated by Bloom

