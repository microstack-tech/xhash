// xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
// Copyright 2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <xhash/version.h>

#include <gtest/gtest.h>

TEST(libxhash, version)
{
    static_assert(xhash::version[0] != 0, "incorrect xhash::version");

    EXPECT_EQ(XHASH_VERSION, TEST_PROJECT_VERSION);
    EXPECT_EQ(xhash::version, TEST_PROJECT_VERSION);
}
