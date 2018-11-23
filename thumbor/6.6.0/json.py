# -*- coding: utf-8 -*-
import rapidjson


def dumps(*args, **kwargs):
    return rapidjson.dumps(*args, number_mode=rapidjson.NM_NATIVE, ensure_ascii=False, **kwargs)


def loads(*args, **kwargs):
    return rapidjson.loads(*args, number_mode=rapidjson.NM_NATIVE, **kwargs)
