import urllib
file_handle = urllib.urlopen('http://python-data.dr-chuck.net/known_by_David.html')
var_A = 0
stack = []
while var_A ==0:
    finding = file_handle.find("href")
    if finding >=0:
        findlen = len(file_handle)
        file_handle = file_handle[finding: findlen]
        finding = file_handle.find('"')
        findlen = len(file_handle)
        file_handle = file_handle[finding+1:findlen]
        finding = file_handle.find('"')
        need = file_handle[0:finding]
        if need.startswith("http" or "www"):
            stack.append(need)
    else:
        var_A = 1
for item in stack:
    print item

