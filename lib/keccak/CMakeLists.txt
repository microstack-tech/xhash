# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# SPDX-License-Identifier: Apache-2.0

include(GNUInstallDirs)

add_library(keccak)
add_library(xhash::keccak ALIAS keccak)
target_compile_features(keccak PUBLIC c_std_99)
set_target_properties(keccak PROPERTIES C_EXTENSIONS OFF)
target_include_directories(keccak PUBLIC $<BUILD_INTERFACE:${include_dir}>$<INSTALL_INTERFACE:include>)
target_sources(keccak PRIVATE
    ${include_dir}/xhash/keccak.h
    ${include_dir}/xhash/keccak.hpp
    keccak.c
)

install(
    TARGETS keccak
    EXPORT xhashTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
