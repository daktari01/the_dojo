'''
fileA = 'fellows_trial.txt'
def file_to_list_converter(afile):
        """Reads a file and returns a list based on the file contents"""
        alist = []
        try:
            for line in open(afile):
                separator = ','
                line = line.read().split(separator)
                for item in alist:
                    alist.append(item)
            return set(alist)
        except:
            raise IOError("File not found")

list_ = list(file_to_list_converter(fileA))
print(list_)
'''
f = open('fellows_trial.txt', 'r')
x = f.readlines()
x = [i.replace('\n','') for i in x]
print(x)

