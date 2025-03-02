#include <PPN-microbench/microbench.hpp>
#include <PPN-microbench/context.hpp>
#include <PPN-microbench/cpu_frequency.hpp>
#include <PPN-microbench/memory.hpp>
#include <PPN-microbench/ops.hpp>

#include <CLI/CLI.hpp>

#include <filesystem>

using json = nlohmann::ordered_json;

class Driver {
  private:
    Context context = Context::getInstance();
    std::vector<Microbench *> benches;
    std::filesystem::path path = std::filesystem::canonical("../report/out.json");
    json results;
    void start();
    void buildJson();

  public:
    Driver();
    Driver(int argc, char ** argv);

    Driver(Driver const & d) = delete;
    Driver(Driver&&) = delete;
    Driver& operator=(const Driver&) = delete;
    Driver operator=(Driver&&) = delete;
    
    ~Driver() {
      for (Microbench *bench : benches) {
          delete bench;
      }
      benches.clear();
    };
    Driver &addBench(Microbench *);
    Driver &setOutputFile(std::string);
    Driver &run();
    Driver &print();
    Driver &save();
};