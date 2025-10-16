# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

cmake_minimum_required(VERSION 3.5)

project(xhash-cmake-config-test)

find_package(xhash CONFIG REQUIRED)

add_executable(xhash-cmake-config-test cmake_config_test.cpp)
target_link_libraries(xhash-cmake-config-test xhash::xhash)
set_target_properties(xhash-cmake-config-test PROPERTIES CXX_STANDARD 11 CXX_EXTENSIONS OFF)
