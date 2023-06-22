### Author Yang, Date 2023/6/21
### Goal: regural calculater
def calculator(P_1, P_2, X_3):
    K = (P_1[2]-P_2[2])/(P_1[1]-P_2[1]) # slope
    Y_3 = K*(X_3-P_1[1])+P_1[2] 
    
    return Y_3, K 