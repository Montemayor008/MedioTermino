meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ python --version
Python 2.7.18
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ rosrun cam_pack image.py
  File "/home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py", line 12
SyntaxError: Non-ASCII character '\xc3' in file /home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py on line 12, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ rosrun cam_pack image.py
  File "/home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py", line 12
SyntaxError: Non-ASCII character '\xc3' in file /home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py on line 12, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ rosrun cam_pack image.py
  File "/home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py", line 12
SyntaxError: Non-ASCII character '\xc3' in file /home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py on line 12, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ rosversion -d
noetic
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack/src$ cd ..
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack$ cd^C
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack$ cd..
cd..: command not found
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src/cam_pack$ cd ..
meli@MeliDell:~/Documents/MedioTermino/catkin_ws/src$ cd ..
meli@MeliDell:~/Documents/MedioTermino/catkin_ws$ catkin_make
Base path: /home/meli/Documents/MedioTermino/catkin_ws
Source space: /home/meli/Documents/MedioTermino/catkin_ws/src
Build space: /home/meli/Documents/MedioTermino/catkin_ws/build
Devel space: /home/meli/Documents/MedioTermino/catkin_ws/devel
Install space: /home/meli/Documents/MedioTermino/catkin_ws/install
####
#### Running command: "cmake /home/meli/Documents/MedioTermino/catkin_ws/src -DCATKIN_DEVEL_PREFIX=/home/meli/Documents/MedioTermino/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/meli/Documents/MedioTermino/catkin_ws/install -G Unix Makefiles" in "/home/meli/Documents/MedioTermino/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/meli/Documents/MedioTermino/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/meli/Documents/MedioTermino/catkin_ws/devel;/opt/ros/noetic
-- This workspace overlays: /home/meli/Documents/MedioTermino/catkin_ws/devel;/opt/ros/noetic
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.8.10", minimum required is "3") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python3
-- Using Debian Python package layout
-- Using empy: /usr/lib/python3/dist-packages/em.py
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/meli/Documents/MedioTermino/catkin_ws/build/test_results
-- Forcing gtest/gmock from source, though one was otherwise available.
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python3 (found version "3.8.10") 
-- Using Python nosetests: /usr/bin/nosetests3
-- catkin 0.8.10
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - cam_pack
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'cam_pack'
-- ==> add_subdirectory(cam_pack)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/meli/Documents/MedioTermino/catkin_ws/build
####
#### Running command: "make -j4 -l4" in "/home/meli/Documents/MedioTermino/catkin_ws/build"
####
meli@MeliDell:~/Documents/MedioTermino/catkin_ws$ source devel/setup.bash
meli@MeliDell:~/Documents/MedioTermino/catkin_ws$ rosrun cam_pack image.py
  File "/home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py", line 12
SyntaxError: Non-ASCII character '\xc3' in file /home/meli/Documents/MedioTermino/catkin_ws/src/cam_pack/src/image.py on line 12, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
meli@MeliDell:~/Documents/MedioTermino/catkin_ws$ cd
meli@MeliDell:~$ cd Documents/
meli@MeliDell:~/Documents$ cd MedioTermino/
meli@MeliDell:~/Documents/MedioTermino$ ls
CMakeLists.txt  Files  Pictures  README.md
meli@MeliDell:~/Documents/MedioTermino$ cd Files/
meli@MeliDell:~/Documents/MedioTermino/Files$ mkdir src
meli@MeliDell:~/Documents/MedioTermino/Files$ cd s
bash: cd: s: No such file or directory
meli@MeliDell:~/Documents/MedioTermino/Files$ cd src/
meli@MeliDell:~/Documents/MedioTermino/Files/src$ catkin_create_pkg image_package 
Created file image_package/package.xml
Created file image_package/CMakeLists.txt
Successfully created files in /home/meli/Documents/MedioTermino/Files/src/image_package. Please adjust the values in package.xml.
meli@MeliDell:~/Documents/MedioTermino/Files/src$ ls
image_package
meli@MeliDell:~/Documents/MedioTermino/Files/src$ cd i
bash: cd: i: No such file or directory
meli@MeliDell:~/Documents/MedioTermino/Files/src$ cd image_package/
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ ls
CMakeLists.txt  package.xml
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ mkdir src
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ mkdir launch
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ ls
CMakeLists.txt  launch  package.xml  src
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ ls
CMakeLists.txt  launch  package.xml  src
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ cd src
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package/src$ ls
image.py
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package/src$ cd ..
meli@MeliDell:~/Documents/MedioTermino/Files/src/image_package$ cd ..
meli@MeliDell:~/Documents/MedioTermino/Files/src$ cd ..
meli@MeliDell:~/Documents/MedioTermino/Files$ catkin_make
Base path: /home/meli/Documents/MedioTermino/Files
Source space: /home/meli/Documents/MedioTermino/Files/src
Build space: /home/meli/Documents/MedioTermino/Files/build
Devel space: /home/meli/Documents/MedioTermino/Files/devel
Install space: /home/meli/Documents/MedioTermino/Files/install
Creating symlink "/home/meli/Documents/MedioTermino/Files/src/CMakeLists.txt" pointing to "/opt/ros/noetic/share/catkin/cmake/toplevel.cmake"
####
#### Running command: "cmake /home/meli/Documents/MedioTermino/Files/src -DCATKIN_DEVEL_PREFIX=/home/meli/Documents/MedioTermino/Files/devel -DCMAKE_INSTALL_PREFIX=/home/meli/Documents/MedioTermino/Files/install -G Unix Makefiles" in "/home/meli/Documents/MedioTermino/Files/build"
####
-- The C compiler identification is GNU 9.4.0
-- The CXX compiler identification is GNU 9.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Using CATKIN_DEVEL_PREFIX: /home/meli/Documents/MedioTermino/Files/devel
-- Using CMAKE_PREFIX_PATH: /home/meli/Documents/MedioTermino/catkin_ws/devel;/opt/ros/noetic
-- This workspace overlays: /opt/ros/noetic
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.8.10", minimum required is "3") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python3
-- Using Debian Python package layout
-- Found PY_em: /usr/lib/python3/dist-packages/em.py  
-- Using empy: /usr/lib/python3/dist-packages/em.py
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/meli/Documents/MedioTermino/Files/build/test_results
-- Forcing gtest/gmock from source, though one was otherwise available.
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python3 (found version "3.8.10") 
-- Found Threads: TRUE  
-- Using Python nosetests: /usr/bin/nosetests3
-- catkin 0.8.10
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - image_package
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'image_package'
-- ==> add_subdirectory(image_package)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/meli/Documents/MedioTermino/Files/build
####
#### Running command: "make -j4 -l4" in "/home/meli/Documents/MedioTermino/Files/build"
####
meli@MeliDell:~/Documents/MedioTermino/Files$ source devel/setup.bash
meli@MeliDell:~/Documents/MedioTermino/Files$ rosrun image_package image.py 
[ WARN:0] global ../modules/videoio/src/cap_gstreamer.cpp (935) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1

