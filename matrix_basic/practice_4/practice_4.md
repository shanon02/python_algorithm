### **문제**  
`mat` 정사각형 2차원배열이 주어질 때, 대각선의 합을 반환하라.  
대각선의 합에는 메인 대각선의 합과 보조 대각선의 합이다 (보조 대각선의 요소 중에 메인 대각선에 포함하는 요소는 제외 )

### **제한사항**
- n == mat.length == mat[i].length
- 1 <= n <= 100
- 1 <= mat[i][j] <= 100
### **예시**  
<hr/>

***Example 1***:
![img](https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png)
**Input**: *mat = [[**1**,2,**3**],
              [4,**5**,6],
              [**7**,8,**9**]]*  
**Output**: *25*
###### 설명: 
###### 대각선의 합: 1 + 5 + 9 + 3 + 7 = 25
###### mat[1][1] = 5는 오직 한 번만 센다.
<hr/>

***Example 2***:

**Input**: *mat = [[**1**,1,1,**1**],
              [1,**1**,**1**,1],
              [1,**1**,**1**,1],
              [**1**,1,1,**1**]]*  
**Output**: *8*
<hr/> 

***Example 3***:

**Input**: *mat = [[5]]*  
**Output**: *5*
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/matrix-diagonal-sum/description/]