import contextlib


class Connection:
    def __init__(self):
        self.xid = 0

    def start_transaction(self):
        print("start transaction", self.xid)
        result = self.xid
        self.xid += 1

        return result

    @staticmethod
    def commit_transaction(xid):
        print("Committing transaction", xid)

    @staticmethod
    def rollback_transaction(xid):
        print("Rollback transaction.", xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn.start_transaction()

    def commit(self):
        self.conn.commmit_transaction(self.xid)

    def rollback(self):
        self.conn.rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    transaction = Transaction(connection)
    try:
        yield transaction
    except Exception as e:
        transaction.rollback()
        raise

    transaction.commit()


connection_db = Connection()


with start_transaction(connection_db) as c_db:
    print(c_db)
    raise LookupError("Bad lookup.")