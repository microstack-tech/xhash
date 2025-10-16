# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2021 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

add_library(experimental STATIC)
add_library(xhash::experimental ALIAS experimental)
target_link_libraries(experimental PUBLIC xhash::xhash)
target_sources(
    experimental PRIVATE
    difficulty.cpp
    difficulty.h
)
