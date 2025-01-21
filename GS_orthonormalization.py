import numpy as np

#calculate the coeficient v2Tv1/v1Tv1
def gs_coef(v1,v2):
    return np.dot(v2,v1)/np.dot(v1,v1)

#multiply a coeficient with a vector 
def mul(coef, v):
    return map((lambda x: x*coef),v)

#calculate the projection
def proj(v1,v2):
    return mul(gs_coef(v1,v2),v1)

#iterate to calculate orthonormal vector
def gs(arr_of_vector):
    
    arr_of_ortho_vector = []
    
    for v in range(len(arr_of_vector)):
        current_vec = arr_of_vector[v]
        #as more ortho vector is in the array, this part will be run more correspondingly
        for i in arr_of_ortho_vector:
            proj_vec = proj(i, current_vec)
            current_vec = list(map(lambda x,y : x - y, current_vec,proj_vec))
            
        arr_of_ortho_vector.append(current_vec)
        
    return arr_of_ortho_vector

def main():
    #initialize vectors
    v1 = [2,1,-1]
    v2 = [1,1,0]
    v3 = [0,-1,1]
    
    given_vec = np.array([v1,v2,v3])

    print (np.array(gs(given_vec)))

if __name__ == "__main__":
    main()