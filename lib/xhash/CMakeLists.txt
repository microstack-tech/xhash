# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

include(GNUInstallDirs)

add_library(xhash)
add_library(xhash::xhash ALIAS xhash)
target_compile_features(xhash PUBLIC c_std_11 cxx_std_14)
set_target_properties(xhash PROPERTIES C_EXTENSIONS OFF CXX_EXTENSIONS OFF)
target_link_libraries(xhash PRIVATE xhash::keccak xhash::sha3)
target_include_directories(xhash PUBLIC $<BUILD_INTERFACE:${include_dir}>$<INSTALL_INTERFACE:include>)
target_sources(xhash PRIVATE
    endianness.hpp
    ${include_dir}/xhash/xhash.h
    ${include_dir}/xhash/xhash.hpp
    xhash-internal.hpp
    xhash.cpp
    ${include_dir}/xhash/hash_types.h
    primes.h
    primes.c
)


if(CABLE_COMPILER_GNULIKE AND NOT MSVC AND NOT SANITIZE MATCHES undefined)
  target_compile_options(xhash PRIVATE $<$<COMPILE_LANGUAGE:CXX>:-fno-rtti>)
endif()

install(
    TARGETS xhash
    EXPORT xhashTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
