# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2018 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

include(GoogleTest)

hunter_add_package(GTest)
find_package(GTest CONFIG REQUIRED)

add_executable(
    xhash-test
    helpers.hpp
    test_cases.hpp
    test_difficulty.cpp
    test_xhash.cpp
    test_keccak.cpp
    test_sha3.cpp
    test_global_context.cpp
    test_primes.cpp
    test_version.cpp
)

set_source_files_properties(test_version.cpp PROPERTIES COMPILE_DEFINITIONS TEST_PROJECT_VERSION="${PROJECT_VERSION}")

target_link_libraries(xhash-test PRIVATE xhash::global-context xhash::experimental GTest::gtest_main)
target_include_directories(xhash-test PRIVATE ${XHASH_PRIVATE_INCLUDE_DIR})
set_target_properties(xhash-test PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)

if(SANITIZE AND CMAKE_SYSTEM_NAME STREQUAL Linux AND CMAKE_CXX_FLAGS MATCHES -m32)
  # Workaround for linking with phread when building for 32-bit and with sanitizer.
  target_link_libraries(xhash-test PRIVATE pthread)
endif()

gtest_discover_tests(xhash-test TEST_PREFIX ${PROJECT_NAME}/unittests/)
