#!/usr/bin/python
# -*- coding: utf-8 -*-
import leancloud

from leancloud import Object
from leancloud import Query

from mdat.config import APP_ID, APP_KEY
from mdat.config import DV_DEFAULT, DV_STEP


def _get_tag_from_leancloud(title):
    """
    leancloud 中获取title 的tag
    :param title:
    :return:
    """
    leancloud.init(APP_ID, APP_KEY)
    Mesh = Object.extend('MESH')
    query = Query(Mesh)
    query.equal_to('title', title)
    objects = query.find()
    results = []

    for obj in objects:
        results.append(obj.attributes['tag'])
    return results


def get_mesh_tags_by_title(title):
    """
    根据疾病的title 获取数据库中的疾病的所有tags
    :param title: 'Pacific Ocean'
    :return: ['Z01.756.700']
    """
    return _get_tag_from_leancloud(title)


def calculate_dv_value(tags):
    """
    计算一个疾病的tags的DV值
    :param tags:
    :return:
    """
    _current_value = DV_DEFAULT
    for tag in tags:
        # tag is 'C04.588.180'
        items = tag.split('.')
        for i in range(len(items) - 1):
            _current_value += pow(DV_STEP, i + 1)

    return _current_value


def calculate_dv_value_by_disease(tags, disease_tags):
    """
    计算由于部分的集合 与疾病的tags的DV值
    :param tags:
    :param disease_tags:
    :return:
    """
    _current_value = 0
    for tag in tags:
        for disease_tag in disease_tags:
            i = calculate_disease_multiple(tag, disease_tag)
            if i != 0:
                _current_value += pow(DV_STEP, i)

    return _current_value


def generate_disease_set(tags):
    """
    生成疾病tags 的所有父类的tags
    :param tags:
    :return:
    """
    generate_set = []
    for tag in tags:
        items = tag.split('.')

        _current = None
        for item in items:

            if not _current:
                _current = item

            else:
                _current += '.' + item

            if _current not in generate_set:
                generate_set.append(_current)

    return generate_set


def calculate_disease_multiple(tag_a, tag_b):
    """
    计算 两个疾病之间的倍数
    例如：
        'Z01' 'Z01.11' 相差一倍
        'Z01' 'Z01.11.121' 相差两倍

    :param tag_a: 疾病A 的tag
    :param tag_b: 疾病B 的tag
    :return: 返回这两者之间相差的倍数
    """

    if tag_a not in tag_b:
        return 0

    items = tag_b.split('.')
    _current = None

    for index, item in enumerate(items):
        if not _current:
            _current = item
        else:
            _current += '.' + item

        if _current == tag_a:
            return len(items) - index - 1


def calculate_dv_similarity(disease_a, disease_b):
    """
    计算两种疾病的DV相似度
    :param disease_a: 'Pacific Ocean'
    :param disease_b: 'Indian Ocean'
    :return:
    """
    if disease_a == disease_b:
        return 1.0

    disease_a_tags = get_mesh_tags_by_title(disease_a)
    disease_b_tags = get_mesh_tags_by_title(disease_b)

    a_dv_value = calculate_dv_value(disease_a_tags)
    b_dv_value = calculate_dv_value(disease_b_tags)

    a_generate_set = generate_disease_set(disease_a_tags)
    b_generate_set = generate_disease_set(disease_b_tags)

    a_b_common = []
    for item in a_generate_set:
        if item in b_generate_set:
            a_b_common.append(item)

    a_similar_dv = calculate_dv_value_by_disease(a_b_common, disease_a_tags)
    b_similar_dv = calculate_dv_value_by_disease(a_b_common, disease_b_tags)

    return (a_similar_dv + b_similar_dv) / (a_dv_value + b_dv_value)
