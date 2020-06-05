<html>
<title>Bitwise AND of Numbers Range</title>
<head>
      <style type="text/css">
	  h1{color:red;}
	   h2, h3, h4{font-size:20px;
		               color:75263D;
					   font-style:italic;}	
	   table{border:#9EECED;}
	   td{background-color:#F8FAC3;}				   
	  </style>
</head>
<body>
<h1>leetcode day23 question<h1>
<h3>Bitwise AND of Numbers Range</h3>
<pre class="tab">
<p>
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

</p></pre>
</br>

<h2>Python solution</h2>
<table border="1">
<td>
<pre class="tab">
<p>
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift=0
        while m!=n:
            m >>=1
            n >>=1
            shift +=1
        return m << shift    
</p>
</pre>
</td>
</table>
</body>
</html>