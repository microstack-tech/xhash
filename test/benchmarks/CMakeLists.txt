# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

hunter_add_package(benchmark)
find_package(benchmark CONFIG REQUIRED)

add_executable(xhash-bench
    xhash_benchmarks.cpp
    keccak_benchmarks.cpp
    keccak_utils.hpp
    keccak_utils.cpp
    global_context_benchmarks.cpp
    threadsync_benchmarks.cpp
    threadsync_utils.hpp
    threadsync_utils.cpp)
target_link_libraries(xhash-bench PRIVATE xhash::global-context benchmark::benchmark)
target_include_directories(xhash-bench PRIVATE ${XHASH_PRIVATE_INCLUDE_DIR})
set_target_properties(xhash-bench PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
