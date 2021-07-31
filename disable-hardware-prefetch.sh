#!/bin/bash

# TODO: detect CPU and twiddle appropriate MSRs.

# Prefetch on newer intel architectures.
# see https://software.intel.com/content/www/us/en/develop/articles/disclosure-of-hw-prefetcher-control-on-some-intel-processors.html
wrmsr -a 0x1a4 15
# On older Core and NetBurst:
# see https://software.intel.com/content/www/us/en/develop/articles/optimizing-application-performance-on-intel-coret-microarchitecture-using-hardware-implemented-prefetchers.html
MSRORIG=$(printf "0x%x\n" $(rdmsr -c 0x1a0)) 
wrmsr -a 0x1a0 $((MSRORIG | 1<<19 | 1<<9))
# to enable again:
#  wrmsr -a 0x1a0 $((MSRORIG & ~(1<<19 | 1<<9)))
