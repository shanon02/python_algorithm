### **문제**  
아래 조건을 만족하는 `X-Matrix` 라고 불리는 정사각형 2차원 배열이 있다.  
1. 대각선에 있는 모든 요소는 0이 아니다.  
2. 대각선 외에 있는 모든 요소는 0 이다.  

`n * n` 사이즈의 정사각형 2차원 배열 `grid`가 주어질 때, X-Matrix면 `True`, 아니면 `False`를 반환하라. 
### **제한사항**
- n == grid.length == grid[i].length  
- 3 <= n <= 100  
- 0 <= grid[i][j] <= 10<sup>5</sup>
### **예시**  
<hr/>

***Example 1***:

**Input**: *grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]*  
**Output**: *True*
###### 설명: 
![img](https://assets.leetcode.com/uploads/2022/05/03/ex1.jpg)
###### 위의 2차원 배열보자.
###### X-matrix는 초록색 요소들이 0이 아니여야하고, 빨간 요소들은 0이여야 한다.
###### 그래서 위 2차원 배열은 X-Matrix이다.
<hr/>

***Example 2***:

**Input**: *grid = [[5,7,0],[0,3,1],[0,5,0]]*  
**Output**: *False*
###### 설명:
![img](https://assets.leetcode.com/uploads/2022/05/03/ex2.jpg)
###### 위의 2차원 배열보자.
###### X-matrix는 초록색 요소들이 0이 아니여야하고, 빨간 요소들은 0이여야 한다.
###### 그래서 위 2차원 배열은 X-Matrix가 아니다.  
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/]
