from __future__ import annotations

from polyeval.generators.base import *


class NamingGeneratorCpp(NamingGeneratorBase):
    global_func_naming = "camelCase"
    global_var_naming = "snake_case"
    member_func_naming = "camelCase"
    member_var_naming = "snake_case"
    arg_naming = "snake_case"
    temp_var_naming = "snake_case"
