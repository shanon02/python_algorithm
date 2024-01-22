### **문제**  
`m * n` 크기의 정수 2차원 배열 `accounts` 가 주어진다.  
`accounts[i][j]` 는 i<sup>th</sup> 고객이 j<sup>th</sup> 은행에 있는 돈이다.  
가장 부유한 고객이 가지고 있는 총액을 리턴하세요.

고객의 총액은 그들의 은행에 있는 모든 돈을 합한 금액이다. 
### **제한사항**
- m == accounts.length
- n == accounts[i].length
- 1 <= m, n <= 50
- 1 <= accounts[i][j] <= 100
### **예시**  
<hr/>

***Example 1***:

**Input**: *accounts = [[1,2,3],[3,2,1]]*  
**Output**: *6*
###### 설명: 
###### 첫 번째 고객의 총액은 1 + 2 + 3 = 6
###### 두 번째 고객의 총액은 3 + 2+ 1 = 6
###### 두 고객 모두 총액은 최고 6이다. 그러므로 가장 부자의 총액은 6 이다
<hr/>

***Example 2***:

**Input**: *accounts = [[1,5],[7,3],[3,5]]*  
**Output**: *10*
###### 설명:
###### 첫 번째 고객의 총액은 6
###### 두 번째 고객의 총액은 10
###### 세 번째 고객의 총액은 8
###### 두 번째 고객의 총액이 가장 크므로 가장 부자의 총액은 10 이다.
<hr/> 

출처: 릿코드 [https://leetcode.com/problems/richest-customer-wealth/description/]
