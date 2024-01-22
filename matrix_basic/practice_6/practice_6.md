### **문제**  
`m * n` 이진 배열 `mat` 이 주어질 때, `mat` 에서 특별한 위치의 수를 구하라.  
특별한 `(i, j)` 는 `mat[i][j] == 1` 이고, 나머지 모든 `i열`과 `j열`의 요소들은 `0`이다.  
### **제한사항**
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- mat[i][j] 은 0 이거나 1 이다.
### **예시**  
<hr/>

***Example 1***:
![img](https://assets.leetcode.com/uploads/2021/12/23/special1.jpg)

**Input**: *mat = [[1,0,0],[0,0,1],[1,0,0]]*  
**Output**: *1*
<hr/>

***Example 2***:
![img](https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg)

**Input**: *mat = [[1,0,0],[0,1,0],[0,0,1]]*  
**Output**: *3*
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/]
