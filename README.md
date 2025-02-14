# GP Symbolic Regression 

The algorithm ia a gp  generational with elitism, the representation of the the formulas are trees
The parent selection is random, the plan was to go with fitness proportional but even leveraging numpy is too 
computationally expensive, so we mimic a similar behaviour with 20% elitism ,
over a lot generation the best perfoming individuals will be the ones who reproduce the most.
Tree depth is limited to avoid overfitting and bloating, in case a genetic opertator produces bigger trees than 
max_depth a parent is returned

The final solution is cherry picked from multiple runs considering MSE and complexity of the functions 

The solution is a collaborative work with my collegue Luca bergamini 

Other deatails of the code are comments in the code 
