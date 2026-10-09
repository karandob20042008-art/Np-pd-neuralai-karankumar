import numpy as np
# questrion 4

x=np.array([[1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6]])
y=np.array([3,5,7,9,11])

# part 1
x=np.c_[np.ones((5,1), int),x]
# print(x_bias)
#part 2
xt_x=x.T @ x
#part 3
xt_y=x.T @ y
#part 4
w= np.linalg.pinv(xt_x) @ xt_y
#part 5
y_pred=x @ w
#part6
error=y-y_pred
square_error= error**2
mse= np.mean(square_error)
#part 7
print("hello\n world")
print(w,"\n",y_pred,"\n",mse)
