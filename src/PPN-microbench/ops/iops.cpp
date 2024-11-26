#include <PPN-microbench/ops/iops.hpp>

void Iops::compute(int cpu) {
    pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);

    long long sum = 0;

    u64 opsPerLoop = 25;
    i64 i[25] = {
        675804981625017, 712754860957697, 394053602764455, 820993044344894,
        208100954703234, -60002541372275, -10938368667033, -69067871329563,
        -60112960571491, -60908980612608, 384152016250026, 355892348048323,
        811168134827124, 588242502359115, 731348774920066, -50888274656573,
        -35482044204805, -58332992093342, -39064238289434, -23710606297884,
        923944050213589, 697930930079161, 111695701329434, 385655241738257,
        483928688142021,
    };

    while (1) {
        // if ((results[cpu] % 10000000000) == 0) std::cout << results[cpu] <<
        // std::endl;

        sum += i[1] * i[2] + i[3] * i[4] + i[5] * i[6] + i[7] * i[8] +
               i[9] * i[10] + i[11] * i[12] + i[13] * i[14] + i[15] * i[16] +
               i[17] * i[18] + i[19] * i[20] + i[21] * i[22] + i[23] * i[24];
        results[cpu] += opsPerLoop;
    }
}