import sqlparse
raw = "SELECT \
a.uid, b.uname \
FROM \
(select * from user) a, \
(select * from user_details) b;"
parsed =  sqlparse.parse(raw)[0]
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
tbl_nms=""
tbl_alias=""
col_alias=""
tbl_cols={}

        
for C in col_split :
        col_alias=C.split(".")[0]
        if len(col_alias) :
           col_nm=C.split(".")[1]
        else :
           col_nm=C
        #print(col_alias+"***")
        for T in tbl_split :
            if "(" in T and ")" in T :
                tbl_alias = T.split(")")[1]
                tbl_nm = T.split(")")[0].split()[-1]
                
            else :
                tbl_alias = ""
                tbl_nm = T
            #print(tbl_alias+"###")
            if col_alias.strip() == tbl_alias.strip() :
                #print(col_alias,tbl_alias)
                tbl_cols[col_nm] = tbl_nm
                break
                
            elif len(col_alias) == 0 :
                tbl_cols[col_nm] = tbl_nm
                break
                
            
   
for key in tbl_cols:
    print(key,"=>",tbl_cols[key])


    
