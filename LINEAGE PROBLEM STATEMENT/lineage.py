import sqlparse
raw = "SELECT a.uid, b.uname \
FROM (select * from user) a, \
(select * from user_details) b;"
parsed =  sqlparse.parse(raw)[0]
token1 = []
prev = ""
cols = ""
tbls = ""
for i in parsed.tokens :
    if str(i).isspace():
        continue
    str1 = str(i).strip().upper()
    if (prev == "SELECT") :
        cols = str1
    elif (prev == "FROM") :  
        tbls = str1
        break
    prev = str1
col_split=cols.split(",")
tbl_split=tbls.split(",")
tbl_nms=[]
tbl_alias=[]
for T in tbl_split :
    if "(" in T and ")" in T :
        print(T.split(")")[1])
        tbl_nms[T.split(")")[1]] = [ i[-1] for i in T.split(")")[0] ]
        #tbl_nms.append(T.split(")")[0])
        #print(str1)
    else :
        tbl_nms.append(T[0])
print(tbl_nms)
        
        
    

