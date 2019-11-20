# Graph
To get any graph, import 
<b>getGraph(dd, mm, yy, dOffset,graphType)</b> function from getAPIData 
<br>

* To get the <b>COMPOSITE</b> graph object: <br>
 Suppose you want a COMPOSITE graph for 10 days from date February 9, 2009 then :<br>
 <h5>Inputs: </h5>
dd = 9  <br>
mm = 2 <br>
yy = 2009  <br>
dOffset = 10 <br>
graphType = COMPOSITE
<h5>Output: </h5>
Two values will be returned:<br>
 "Success"/"Fail"<br>
 The composite graph in the form of object of <b>MultiDiGraph</b>


![Image of Composite graph](composite.png)





<h3>Inputs: </h3>
<b>graphType</b> may take one of the three values :<br>
<ul>
<li>COMPOSITE
<li>ADDRESS
<li>TRANSACTION
</ul>
dirPath = "../XYZ"

<h3>Output:</h3>
<ul>
<li>
In case of <b>COMPOSITE </b> graph you will get an edge list file at the given directory path("../XYZ")
<br>
<li>
In case of <b>ADDRESS</b> graph you will get an edge list file and a vertex list file at the given directory path("../XYZ")
<br>
<li>
In case of <b>TRANSACTION</b> graph you will get an edge list file and a vertex list file at the given directory path("../XYZ")
</ul>