# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

find_package(Threads)

add_executable(xhash-fakeminer fakeminer.cpp)
target_link_libraries(xhash-fakeminer PRIVATE xhash::global-context Threads::Threads)
set_target_properties(xhash-fakeminer PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
