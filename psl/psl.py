class psl_(object):
    def __init__(self):
        self.last_len = None

    def __call__(self, *args, **kwargs):
        s = " ".join([str(x) for x in args])
        if self.last_len is not None:
            print(" " * self.last_len, end="\r", flush=True)
        self.last_len = len(s)
        print(s, end="\r", flush=True)


psl = psl_()
