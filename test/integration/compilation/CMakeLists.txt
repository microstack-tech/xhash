# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2018-2020 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

file(GLOB c_sources ${PROJECT_SOURCE_DIR}/lib/xhash/*.c)

foreach(c_std 0 99 11)
    set(target test-compile-c${c_std})
    add_library(${target} STATIC xhash_header_test.c ${c_sources})
    target_link_libraries(${target} PRIVATE xhash::xhash)
    if(c_std)
        set_target_properties(${target} PROPERTIES C_STANDARD ${c_std})
    endif()
    set_target_properties(${target} PROPERTIES C_EXTENSIONS OFF)
endforeach()
