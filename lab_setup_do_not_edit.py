import sys
import os
import importlib
from IPython import get_ipython


def _aggressive_reloader(info):
    """INTERNAL TOOL: Scans for local modules and reloads them."""
    current_dir = os.getcwd()
    modules_to_reload = []

    for name, module in sys.modules.items():
        if not hasattr(module, "__file__") or module.__file__ is None:
            continue

        module_path = os.path.abspath(module.__file__)

        if module_path.startswith(current_dir):
            if "lab_setup_do_not_edit" in name:
                continue
            modules_to_reload.append(module)

    for _ in range(2):
        for module in modules_to_reload:
            try:
                importlib.reload(module)
            except Exception:
                pass


def _activate_autoreload():
    ip = get_ipython()

    if ip is None:
        return

    try:
        ip.events.unregister("pre_run_cell", _aggressive_reloader)
    except ValueError:
        pass

    ip.events.register("pre_run_cell", _aggressive_reloader)
    print("✅ Environment ready! Code will update automatically.")


_activate_autoreload()
