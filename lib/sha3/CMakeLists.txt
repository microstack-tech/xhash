# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# SPDX-License-Identifier: Apache-2.0

include(GNUInstallDirs)

add_library(sha3)
add_library(xhash::sha3 ALIAS sha3)
target_compile_features(sha3 PUBLIC c_std_99)
set_target_properties(sha3 PROPERTIES C_EXTENSIONS OFF)
target_include_directories(sha3 PUBLIC $<BUILD_INTERFACE:${include_dir}>$<INSTALL_INTERFACE:include>)
target_sources(sha3 PRIVATE
    ${include_dir}/xhash/sha3.h
    ${include_dir}/xhash/sha3.hpp
    sha3.c
)

install(
    TARGETS sha3
    EXPORT xhashTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
