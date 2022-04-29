print("     Dictionary elements")
print("-----------------------------------")
dic1={"color":"blue","fruit":"banana","veg":"carrot"}
print("dictionary dic1 elements : ", dic1)

print("\n   DICTIONARY OPERATIONS")
print("-----------------------------------")

print("1.datatype \n2.length of the dictionary \n3.add items to the dictionary \n4.update the value of a key \n5.create a copy of the dictionary \n6.remove items from the dictionary \n7.display only keys \n8.display only values \n9.display full dictionary using for loop \n10.check elements existance")

n=int(input("\nenter your choice : "))

if(n==1):
  print("datatype of dic1 is : ",type(dic1));
elif(n==2):
  print("number of element in the dictionary dic1 is : ",len(dic1))
elif(n==3):
  a=input("Enter the key:")
  b=input("Enter the value:")
  print("dic1 before adding an element : ",dic1)
  dic1[a]=b
  print("an element is added to the dic1 : ",dic1)
elif(n==4):
  a=input("Enter key:")
  b=input("Enter value to update:")
  print("dic1 before updating value : ",dic1)
  dic1[a]=b
  print("Updated dictionary : ",dic1)
elif(n==5):
  dic2=dic1.copy()
  print("dic1 is copied to dic2 \ndic2 : ",dic2)
elif(n==6):
  a=input("Enter any key element to delete")
  print("dic1 before deleting an element : ",dic1)
  del dic1[a]
  print("an item deleted dic1 : ",dic1)
elif(n==7):
  dic1.clear()
  print("all items deleted from dic1 : ",dic1)
elif(n==8):
  print("keys in dic1 :")
  for i in dic1.keys():
    print ("key--", i)
elif(n==9):
  print("values in dic1 :")
  for i in dic1.values():
    print ("value--", i)
elif(n==10):
  print("all the items in dic1 : ")
  for k,v in dic1.items():
    print(k," relates to ", v)
elif(n==11):
  e=str(input("enter an element to check for existence : "))
  if (dic1.get(e)==None):
    print ("no such element")
  else:
    print("element exist");
else:
  print("INVALID CHOICE!!")
