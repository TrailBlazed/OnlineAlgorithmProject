from collections import defaultdict
from urllib.request import urlopen
import os
import ijson
BLOCK_URL = "https://blockchain.info/rawblock/"

graph = defaultdict(list)

def get_block_data():
    """
    Method to get block data
    """
    try:
        trans_count = 0
        count = 0
        block_hash1 = "00000000000002e3269b8a00caf315115297c626f954770e8398470d7f387e1c"
        block_hash = "000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214"
        file_path = os.path.join(r'/home/sarada/PycharmProjects/OnlineProject', block_hash + ".txt")
        if os.path.isfile(file_path):
            os.remove(file_path)
        while count < 20:
            url = BLOCK_URL + block_hash
            response = urlopen(url)
            res2 = urlopen(url)
            next_block = ijson.items(res2,'next_block.item')
            for read_next in next_block:
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
                #print(str(k) + testlist)
                writer.write(str(k) + testlist + "\n")

    except Exception as e:
        return 'Fail',e
    return 'Success',file_path

if __name__ == '__main__':
    result, path = get_block_data()
    print(result)
    print(path)