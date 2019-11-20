# Graph
To get any graph, import 
<b>getGraph(dd, mm, yy, dOffset,graphType)</b> function from getAPIData. 
<br>

![Image of Composite graph](images/composite.png)
* To get the <b>COMPOSITE</b> graph object: <br>
 Suppose you want a COMPOSITE graph for 10 days from date February 9, 2009 then :<br>
    * Inputs: <br> 
dd = 9  <br>
mm = 2 <br>
yy = 2009  <br>
dOffset = 10 <br>
graphType = COMPOSITE
    * Output:
Two values will be returned:<br>
 "Success"/"Fail"<br>
 The composite graph in the form of object of <b>MultiDiGraph</b>
    * Here, edges of the graph will be of 2 types:
        * "From:" Address, "To:" Transaction hash, Amount
        * "From:" Transaction hash, "To:" Address, Amount

One can differentiate Transaction hash by its length, which is 64.
   

![Image of Address graph](images/address.png)

* To get the <b>ADDRESS</b> graph object: <br>
 Suppose you want a ADDRESS graph for 10 days from date February 9, 2009 then :<br>
    * Inputs: <br> 
dd = 9  <br>
mm = 2 <br>
yy = 2009  <br>
dOffset = 10 <br>
graphType = ADDRESS
    * Output:
Two values will be returned:<br>
 "Success"/"Fail"<br>
 The address graph in the form of object of <b>MultiDiGraph</b>
    * Here, edges of the graph will be of only 1 type:
        * "From:" Address, "To:" Address, Amount
      

![Image of Address graph](images/transaction.png)

* To get the <b>TRANSACTION</b> graph object: <br>
 Suppose you want a TRANSACTION graph for 10 days from date February 9, 2009 then :<br>
    * Inputs: <br> 
dd = 9  <br>
mm = 2 <br>
yy = 2009  <br>
dOffset = 10 <br>
graphType = TRANSACTION
    * Output:
Two values will be returned:<br>
 "Success"/"Fail"<br>
 The transaction graph in the form of object of <b>MultiDiGraph</b>
    * Here, edges of the graph will be of only 1 type:
        * "From:" Transaction, "To:" Transaction, Amount
      