import sys

# 1 : 벽 (#) // 0 : 흰칸 (.)

board = [[1 for col in range(20)] for row in range(20)]

def main():

  case = input('case 수 입력 : ')
  caseNum = int(case)
  
  for  i in range (0, caseNum):
    hw = input().split(" ")
    height = hw[0]
    weight = hw[1]
    for j in range(0, int(weight)):
      line = input()
      


    print(hw, height, weight)
    print(line[:int(weight)])

if __name__ == "__main__":
  main()

'''
3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 

1
3 7
#.....# 
#.....# 
##...## 

'''