// xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
// Copyright 2018-2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <xhash/xhash.hpp>
#include <xhash/version.h>

int main()
{
    static_assert(sizeof(xhash::version) >= 6, "incorrect xhash::version");

    uint8_t seed_bytes[32] = {0};
    xhash::hash256 seed = xhash::hash256_from_bytes(seed_bytes);
    return xhash::find_epoch_number(seed);
}
