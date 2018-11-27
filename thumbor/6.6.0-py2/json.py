# -*- coding: utf-8 -*-
import ujson


loads = ujson.loads


def dumps(*args, **kwargs):
    return rapidjson.dumps(*args, ensure_ascii=False, **kwargs)
