
import collections

tc_menu = collections.namedtuple("tc_menu", ["title", "icon", "items"])
tc_item = collections.namedtuple("tc_item", ["name", "icon", "command", "background", "run_at_startup", "cwd"])

def new_menu_item(**kwargs):
    default_args = {
            "icon" : None,
            "cwd" : None,
            "background" : False,
            "run_at_startup" : False,
            }
    for (k,v) in default_args.items():
        kwargs.setdefault(k, v)
    return tc_item(**kwargs)

