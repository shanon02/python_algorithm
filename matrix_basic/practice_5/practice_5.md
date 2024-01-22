### **문제**  
2차원 정수 배열 `matrix` 가 주어질 때, 행렬의 전치를 반환하라.  
행렬의 전치란 행렬의 행과 열을 바꿔, 주 대각선을 뒤집는 것이다.
![img](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)
### **제한사항**
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 10<sup>5</sup>
- -10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup>
### **예시**  
<hr/>

***Example 1***:

**Input**: *matrix = [[1,2,3],[4,5,6],[7,8,9]]*  
**Output**: *[[1,4,7],[2,5,8],[3,6,9]]*
<hr/>

***Example 2***:

**Input**: *matrix = [[1,2,3],[4,5,6]]*  
**Output**: *[[1,4],[2,5],[3,6]]*
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/transpose-matrix/description/]
