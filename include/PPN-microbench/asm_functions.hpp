#ifndef PPN_MICROBENCH_ASM_FUNCTIONS_HPP
#define PPN_MICROBENCH_ASM_FUNCTIONS_HPP

#include <cstdint>

extern "C" void cpu_frequency_x86_64(uint64_t iterations);
extern "C" void cpu_frequency_arm_64(uint64_t iterations);

#if defined(__i386__) || defined(__x86_64__)

    extern "C" void ADD_X86_i32(int64_t);
    extern "C" void ADD_X86_i64(int64_t);
    extern "C" void ADD_X86_f32(int64_t);
    extern "C" void ADD_X86_f64(int64_t);

    extern "C" void ADD_X86_i64_SSE(int64_t);
    extern "C" void ADD_X86_f64_SSE(int64_t);

    extern "C" void ADD_X86_i64_AVX(int64_t);
    extern "C" void ADD_X86_f64_AVX(int64_t);

    extern "C" void ADD_X86_i64_AVX512(int64_t);
    extern "C" void ADD_X86_f64_AVX512(int64_t);

    #define ADD_i32 ADD_X86_i32
    #define ADD_i64 ADD_X86_i64
    #define ADD_f32 ADD_X86_f32
    #define ADD_f64 ADD_X86_f64

    #if defined(__SSE2__)
        #define SIMD_INT_MAX_FN ADD_X86_i64_SSE
        #define SIMD_FLOAT_MAX_FN ADD_X86_f64_SSE
    #endif
    #if defined(__AVX__)
        #undef SIMD_FLOAT_MAX_FN
        #define SIMD_FLOAT_MAX_FN ADD_X86_f64_AVX
    #endif
    #if defined(__AVX2__)
        #undef SIMD_INT_MAX_FN
        #define SIMD_INT_MAX_FN ADD_X86_i64_AVX
    #endif
    #if defined(__AVX512F__)
        #undef SIMD_INT_MAX_FN
        #undef SIMD_FLOAT_MAX_FN
        #define SIMD_INT_MAX_FN ADD_X86_i64_AVX512
        #define SIMD_FLOAT_MAX_FN ADD_X86_f64_AVX512
    #endif
#endif

#if defined(__arm__) || defined(__aarch64__)

    extern "C" void ADD_ARM_i32(int64_t);
    extern "C" void ADD_ARM_i64(int64_t);
    extern "C" void ADD_ARM_f32(int64_t);
    extern "C" void ADD_ARM_f64(int64_t);

    extern "C" void ADD_ARM_i64_NEON(int64_t);
    extern "C" void ADD_ARM_f64_NEON(int64_t);

    #define ADD_i32 ADD_ARM_i32
    #define ADD_i64 ADD_ARM_i64
    #define ADD_f32 ADD_ARM_f32
    #define ADD_f64 ADD_ARM_f64

    #if defined(__ARM_NEON)
        #define SIMD_INT_MAX_FN ADD_ARM_i64_NEON
        #define SIMD_FLOAT_MAX_FN ADD_ARM_f64_NEON
    #else
        #define SIMD_INT_MAX_FN ADD_ARM_i64
        #define SIMD_FLOAT_MAX_FN ADD_ARM_f64
    #endif
#endif

#endif