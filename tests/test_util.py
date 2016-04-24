#!/usr/bin/python
# -*- coding: utf-8 -*-


from mdat.util import calculate_dv_similarity, calculate_dv_value, get_mesh_tags_by_title


if __name__ == '__main__':
    print calculate_dv_similarity('ACTH-Secreting Pituitary Adenoma', 'Adenoma')
    a_tags = get_mesh_tags_by_title('Breast Neoplasms')
    print calculate_dv_value(a_tags)
