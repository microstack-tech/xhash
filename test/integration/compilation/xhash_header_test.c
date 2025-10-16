/* xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
 * Copyright 2018 Pawel Bylica.
 * Licensed under the Apache License, Version 2.0.
 */

#include <xhash/xhash.h>

int test(void);

int test(void)
{
    int sum = 0;
    sum += XHASH_EPOCH_LENGTH;
    sum += XHASH_LIGHT_CACHE_ITEM_SIZE;
    sum += XHASH_FULL_DATASET_ITEM_SIZE;
    return sum;
}
