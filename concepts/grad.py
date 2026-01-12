def gradient_descent(x,y,lr=0.01,epochs=3000):
    m=0.0
    b=0.0
    for epoch in range(epochs):
        y_pred=m*x+b
        error=y-y_pred
        cost=np.mean(error**2)

        derivative_wrt_m=-2*np.mean(x*error)
        derivative_wrt_b=-2*np.mean(error)

        b -= derivative_wrt_b*lr
        m -= derivative_wrt_m*lr

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Cost = {cost}, b = {b}, m = {m}")

if __name__=="__main__":
    x=np.array([1,2,3,4,5])
    y=np.array([5,7,9,11,13])
    gradient_descent(x,y)  #we got m=2 and b=3

    
   