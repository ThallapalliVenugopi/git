class open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file=open(self.filename, self.mode)
        return self.file
    def __exit__(self,exe_type,exc_val,traceback):
        self.file.close()
with open_file('contxt.txt','w') as f:
    f.write("i am a venu gopi")
print(f.closed)


