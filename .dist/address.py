ThreeAddressCode = {} # for final output
ThreeAddressCodeCount=0

small_letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letter=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

presidence={'^':1,'*':2,'/':2,'+':3,'-':3}
stack=[] ## for prefix genaration
output=[] #prefix output

stack_for_Ev=[] # stack For prefix evaluation


def stackPopingForParenthesis():  # pop till clossing parentheses
    lenOfStack = len(stack)
    for i in range(lenOfStack):
        if stack[-1] !=')':
            output.append(stack.pop())

        else:  # got closing parentheses
            stack.pop()
            return


### main function ### main function ### main function ### main function


inString = input("give the: ")  # taking the input
final_assign = ""
equation = ""
remove_space = ''   # # taking a variable to keep th string after removing all extra space
for i in inString: # extra space remove
    if i != " ":
        remove_space += i  # extra space remove

final_assign, equation = remove_space.split("=")
equation=equation[::-1]  # reverse string
"""
# x = (b + (b^2 - 4*a*c)) / (2*a)
# here,  final_assign is 'x' and equation='(b + (b^2 - 4*a*c)) / (2*a)'
"""

for i in equation: # prefix


    if (i in capital_letter) or (i in small_letter) or (i>'0' and i<'9'):   # # if oparend or variable the output
        output.append(i)

    elif len(stack)==0 and (i=='^' or i=='*' or i=='/' or i=='-' or i=='+'): # if operator comes , and stack is empty
        stack.append(i)

    elif i==')': # if open paranthesis scanned, push
        stack.append(i)

    elif i=='(': # if close paranthesis scanned, pop untill open paranthesis, push to output
        stackPopingForParenthesis() # calling function for that

    elif i=='^' or i=='*' or i=='/' or i=='-' or i=='+': # if operator comes , and stack is not empty

        if stack[-1]==')': # if top element of stack is paranthesis then just push the operator
            stack.append(i)


        elif presidence[i]<= presidence[stack[-1]]: #grater or equla operator comes --> push
            stack.append(i)


        else: #lower or equal comes, higher pop,lower push
            output.append(stack.pop())
            stack.append(i)




final_lenOfStack= len(stack)
if final_lenOfStack: #if there is remaining in stack
    for i in range(final_lenOfStack):
        output.append(stack.pop())

preFix=output[::-1]#final output
print("prefix:", preFix) ## here prefix is complate
prefix= output # reverse again or non reverse prefix for evaluation purpose



######## evaluation of prefix  or generating the three address code

for i in prefix:
    if (i in capital_letter) or (i in small_letter) or (i>'0' and i<'9'): ## if oparend or variable
        stack_for_Ev.append(i) ## if oparend or variable the push to stack
    elif (i=='^' or i=='*' or i=='/' or i=='-' or i=='+'): # found any operator the calculate or evaluate
        v1=stack_for_Ev.pop()
        v2=stack_for_Ev.pop()
        ThreeAddressCode['t'+str(ThreeAddressCodeCount)]=v1+i+v2## code genarate and save to tem variable
        stack_for_Ev.append('t'+str(ThreeAddressCodeCount)) ## calculate and result save to  stack for next calculation
        ThreeAddressCodeCount+=1 # increase the temp variable count



print("\nThe three Address code:")
ltv='' #get the last temp variable
for i,j in ThreeAddressCode.items():
    print(i,"=",j)
    ltv=i
###finally assign to final_assign variable
print(final_assign,"=",ltv)


print()
######## evaluation of prefix  or generating the three address code

### main function close




"""
testcase:
X= (A+B ^C )*D +E^5
prefix result:+*+A^BCD^E5
"""