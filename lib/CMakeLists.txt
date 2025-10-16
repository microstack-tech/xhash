# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

add_subdirectory(keccak)
add_subdirectory(sha3)

if(XHASH_BUILD_XHASH)
  add_subdirectory(xhash)
endif()

if(XHASH_BUILD_GLOBAL_CONTEXT)
  add_subdirectory(global_context)
endif()

get_filename_component(XHASH_PRIVATE_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR} ABSOLUTE)
set(XHASH_PRIVATE_INCLUDE_DIR ${XHASH_PRIVATE_INCLUDE_DIR} PARENT_SCOPE)
