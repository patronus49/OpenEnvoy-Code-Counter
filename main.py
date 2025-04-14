import sys
import traceback

from counter_orchestrator.counter_orchestrator_factory_manager import CounterOrchestratorFactoryManager


if __name__ == '__main__':
    try:
        counter_orchestrator = CounterOrchestratorFactoryManager().get_counter_orchestrator()
        counter_orchestrator.init_orchestrator()
        counter_orchestrator.run()

    except Exception as e:
        print(e, traceback.format_exc())
        sys.exit()
