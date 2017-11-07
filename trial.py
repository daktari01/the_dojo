
fileA = 'fellows_trial.txt'
def file_to_list_converter(afile):
        """Reads a file and returns a list based on the file contents"""
        alist = []
        try:
            file_ = open(afile, 'r')
            alist = file_.readlines()
            alist = [i.replace('\n','') for i in alist]
            file_.close()
        except:
            raise IOError("File not found")
        alist = list(set(alist))
        return alist

list_ = list(file_to_list_converter(fileA))
print(list_)
'''
f = open('fellows_trial.txt', 'r')
x = f.readlines()
x = [i.replace('\n','') for i in x]
print(x)
'''