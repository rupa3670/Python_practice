print("Buying 1 to 5 apples:")
for i in range(1,6):
    print(i, "apples cost", i*30,"Taka")

fruits_left = 3
while fruits_left>0:
    print(fruits_left,"oranges left")
    fruits_left = fruits_left - 1
print("No oranges left")