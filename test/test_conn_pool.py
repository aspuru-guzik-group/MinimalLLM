import threading

from mllm.cache.conn_pool import ConnPool


def test():
    conn_pool = ConnPool("./test.db")
    conn_pool.max_conn = 5
    def get_conn():
        conn_pool.get_conn()

    for i in range(20):
        thread = threading.Thread(target=get_conn)
        thread.start()