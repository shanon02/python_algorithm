### **문제**  
`m * n` `2차원 배열`이 주어질 때, 만약 2차원 배열이 대각상수 행렬이면 `True`, 아니면 `False`를 반환하세요.   
- 대각상수 행렬이란 왼쪽 위에서 오른쪽 아래로 가는 모든 대각선에 동일한 요소가 있는 경우를 말한다.  
### **제한사항**
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 20
- 0 <= matrix[i][j] <= 99
### **예시**  
<hr/>

***Example 1***:

**Input**: *matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]*  
**Output**: *True*
###### 설명: 
![img](https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg)
###### 위의 2차원 배열에서 대각선은 다음과 같다.
###### "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
###### 각 대각선의 모든 요소들은 같고, 그래서 정답은 True
<hr/>

***Example 2***:

**Input**: *matrix = [[1,2],[2,2]]*  
**Output**: *False*
###### 설명:
![img](https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg)
###### 대각선 "[1, 2]" 이 서로 다른 요소이다. 
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/]
