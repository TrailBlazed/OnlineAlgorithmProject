from collections import defaultdict
from urllib.request import urlopen
import os
import ijson

BLOCK_URL = "https://blockchain.info/rawblock/"
LATEST_BLOCK = "https://blockchain.info/latestblock"
graph = defaultdict(list)


def get_block_data(path):
    """
    Method to get block data
    """
    try:
        trans_count = 0
        count = 0
        res = urlopen(LATEST_BLOCK)
        latest_hash = ijson.items(res, 'hash')
        for h in latest_hash:
            block_hash = str(h)
        file_path = os.path.join(path, block_hash + ".txt")
        if os.path.isfile(file_path):
            os.remove(file_path)
        while count < 2:
            print(block_hash)
            url = BLOCK_URL + block_hash
            response = urlopen(url)
            res2 = urlopen(url)
            prevblock = ijson.items(res2, 'prev_block')
            for read_next in prevblock:
                block_hash = str(read_next)
            objects = ijson.items(response, 'tx.item')
            read_trans = (o for o in objects)
            for prop in read_trans:
                for inp in prop["inputs"]:
                    if "prev_out" in inp:
                        if "addr" in inp["prev_out"]:
                            for out in prop["out"]:
                                if "addr" in out:
                                    graph[inp["prev_out"]["addr"]].append(out["addr"])
                    else:
                        for out in prop["out"]:
                            if "addr" in out:
                                graph[out["addr"]]
                trans_count = trans_count + 1
            count = count + 1
        print(trans_count)
        with open(file_path, 'a') as writer:
            for k, v in graph.items():
                testlist = ""
                for vl in v:
                    testlist = testlist + " " + str(vl)
                # print(str(k) + testlist)
                writer.write(str(k) + testlist + "\n")

    except Exception as e:
        return 'Fail', e
    return 'Success', file_path


if __name__ == '__main__':
    result, path = get_block_data(r"D:\Online Algo\project\graphs\latest")
    print(result)
    print(path)