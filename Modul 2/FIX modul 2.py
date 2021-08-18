import stacks as st
def cek (x):
    stack = st.stack()
    tes = 0
    for cek in x:
        if cek == "(" or cek == "{" or cek == "[":
          st.push(stack, cek)
        elif cek == ")" or cek == "}" or cek == "]":
            if st.isempty(stack):
                return("Tidak Cocok Kurungnya")
                tes = 1
                break
            elif st.peek(stack) == "(" and cek == ")":
                st.pop(stack)
            elif st.peek(stack) == "{" and cek == "}":
                st.pop(stack)
            elif st.peek(stack) == "[" and cek == "]":
                st.pop(stack)
            else:
                return("Tidak Cocok Kurungnya")
                tes = 1
                break
    if st.isempty(stack) and tes ==0:
        return(True)
    elif not st.isempty(stack) and tes == 0:
        return("Kelebihan kurung buka")
        
x=input("masukkan") 
def postfix (x):
    stack = st.stack()
    kurung=[]
    hasil=''
    a=''
    for cek in x:
        if cek == '0' or cek=='1' or cek=='2' or cek=='3' or cek=='4' or cek=='5' or cek=='6' or cek=='7' or cek=='8' or cek=='9':
            hasil+=str(cek)
        else:
            if cek == "(" or cek == "{" or cek == "[":
                kurung.append(cek)
            elif cek=="+" or cek=="-" or cek=="*" or cek==":":
                st.push(stack,cek)
                hasil+=" "
            elif cek==")" or cek=="]" or cek=="}":
                for i in range (st.size(stack)):
                    hasil+=" "
                    a=a+str(st.pop(stack))
                    hasil+=str(a)
                    a=''
    if not st.isempty(stack):
        hasil+=" "
        a=a+str(st.pop(stack))
        hasil+=str(a)
    if st.isempty(stack):
        return hasil
    else:
        return "Tidak Dapat Dioperasikan"

def evaluatePost(x):
    stack=st.stack()
    hasil=''
    for cek in x:
        if cek == '0' or cek=='1' or cek=='2' or cek=='3' or cek=='4' or cek=='5' or cek=='6' or cek=='7' or cek=='8' or cek=='9':
            hasil+= cek
        elif cek == "+":
            b = st.size(stack)
            c=float(float (stack[b-2]) + float (stack[b-1]))
            st.pop(stack)
            st.pop(stack)
            st.push(stack, c)
        elif cek == "-":
            b = st.size(stack)
            c=float(float(stack[b-2]) - float(stack[b-1]))
            st.pop(stack)
            st.pop(stack)
            st.push(stack, c)
        elif cek == "*":
            b = st.size(stack)
            c=float(float(stack[b-2]) * float(stack[b-1]))
            st.pop(stack)
            st.pop(stack)
            st.push(stack, c)
        elif cek == ":":
            b = st.size(stack)
            c=float(float(stack[b-2])/ float(stack[b-1]))
            st.pop(stack)
            st.pop(stack)
            st.push(stack, c)
        elif cek == " ":
            if st.size(hasil)!= 0:
                a = int(hasil)
                st.push(stack,a)
                hasil=''
    return((stack[0]))

print(cek(x))
if cek(x) == True:
    print("Ekspresi Matematika PostFix = " ,postfix(x))
    print("Hasil Evaluasi = " ,evaluatePost(postfix(x)))
else:
    print("Tidak Dapat Dioperasikan")
    

