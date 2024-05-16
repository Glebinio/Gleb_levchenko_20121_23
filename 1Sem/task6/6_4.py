def main():
    def reverse_matrix (l):

        #length oh matrix
        n=len(l)

        #transporation of matrix
        for i in range (n):
            for j in range (i,n):
                l[j][i],l[i][j]=l[i][j],l[j][i]
        
        #reversed of matrix
        for i in range (n):
            for j in range (n):
                l[i]=list(reversed (l[i]))
        return l
    
    assert reverse_matrix([[1,2,3],[4,5,6],[7,8,9]])== [[7,4,1],[8,5,2],[9,6,3]]
    print(reverse_matrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    

if __name__=="__main__":
    main()