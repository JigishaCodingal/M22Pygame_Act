amount=int(input("Enter Amount : "))
n2000=amount//2000
amount=amount%2000
n500=amount//500
amount=amount%500
n100=amount//100
amount=amount%100
n50=amount//50
amount=amount%50
n10=amount//10
amount=amount%10
n1=amount//1
print("Your entered amount",amount,"contains : ")
print("Total 2000 notes :",n2000)
print("Total 500 notes :",n500)
print("Total 100 notes :",n100)
print("Total 50 notes :",n50)
print("Total 10 notes :",n10)
print("Total 1 notes :",n1)
