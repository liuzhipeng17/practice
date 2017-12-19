# -*- coding: utf-8 -*-
import redis



if __name__ == "__main__":

    conn = redis.Redis(host="127.0.0.1", port=6379, db=0)

    if conn.exists("material_category"):
        try:
            conn.delete("material_category")
        except Exception as e:
            print e.message
            exit(1)

    if conn.exists("烧结磁铁分类"):
        try:
            conn.delete("烧结磁铁分类")
        except Exception as e:
            print e.message
            exit(1)

    if conn.exists("粘结磁铁分类"):
        try:
            conn.delete("粘结磁铁分类")
        except Exception as e:
            print e.message
            exit(1)


    signer_type_list = ["烧结钕铁硼磁铁","烧结铁氧体磁铁",
                        "烧结钐钴磁铁","烧结/铸造铝镍钴磁铁",
                        "烧结钐钴磁铁"]
    bonder_type_list = ["粘结模压钕铁硼磁铁","注塑钕铁硼磁铁",
                        "注塑铁氧体磁铁","注塑钐钴磁铁","胶磁磁体",
                        "柔性钕铁硼磁体"]
    try:
        conn.lpush("material_category", "烧结磁铁分类", "粘结磁铁分类")
        conn.lpush("烧结磁铁分类", *signer_type_list)
        conn.lpush("粘结磁铁分类", *bonder_type_list)
    except Exception as e:
        print e.message
        exit(1)



