# xhash: C/C++ implementation of XHash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

# The CFFI build script for xhash library.
# It expects the library is installed in the dist/ directory.
# The installation can be performed by
#
#     cmake . -DCMAKE_INSTALL_PREFIX=dist
#     make
#     make install

from cffi import FFI
import sys

ffibuilder = FFI()

stdlib = []
if sys.platform == 'linux':
    stdlib.append('stdc++')

ffibuilder.set_source(
    "_xhash",
    r"""
    #include <xhash/keccak.h>
    #include <xhash/xhash.h>
    #include <xhash/global_context.h>
     """,
    include_dirs=['include'],
    libraries=['xhash-global-context', 'xhash', 'keccak'] + stdlib,
)

ffibuilder.cdef("""

union xhash_hash256
{
    ...;
    char str[32];
};

union xhash_hash512
{
    ...;
    char str[64];
};

struct xhash_result
{
    union xhash_hash256 final_hash;
    union xhash_hash256 mix_hash;
};


union xhash_hash256 xhash_keccak256(const uint8_t* data, size_t size);

union xhash_hash512 xhash_keccak512(const uint8_t* data, size_t size);

const struct xhash_epoch_context* xhash_get_global_epoch_context(int epoch_number);

struct xhash_result xhash_hash(const struct xhash_epoch_context* context,
    const union xhash_hash256* header_hash, uint64_t nonce);
    
bool xhash_verify_against_boundary(const struct xhash_epoch_context* context,
    const union xhash_hash256* header_hash, const union xhash_hash256* mix_hash, uint64_t nonce,
    const union xhash_hash256* boundary);

""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
