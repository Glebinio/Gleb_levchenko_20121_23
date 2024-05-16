def main():
    def reverse_matrix (l):
        
        list1=[]
        left,top=0,0
        right,botom=len(l[1])-1,len(l)-1
        i,j,k=0,0,0
        # цикл пока не достигли границы сирали
        while k==0:
            # движение в право
            if right != 0 and k==0:
                while j< right+1:
                    list1.append(l[i][j])
                    j+=1
                right-=1
                i+=1
                j-=1
                # проверка правой границы
                if right==0:
                    k=1
            # движение вниз
            if botom != 0 and k==0:
                while i<botom+1:
                    list1.append(l[i][j])
                    i+=1
                botom-=1
                j-=1
                i-=1
                # проверка нижней границы
                if botom==0:
                    k=1
            # движение влево
            if left != len(l[1])-1 and k==0:
                while j>left-1:
                    list1.append(l[i][j])
                    j-=1
                left+=1
                i-=1
                j+=1
                # проверка левой границы
                if left==0:
                    k=1
            # движение вверх
            if top != len(l)-1 and k==0:
                while i>top:
                    list1.append(l[i][j])
                    
                    i-=1
                top+=1
                i+=1
                j+=1
                # проверка верхней границы
                if top==0:
                    k=1
        return list1
        
    
    assert reverse_matrix ([[1,2,3],[4,5,6],[7,8,9]])==[1,2,3,6,9,8,7,4,5]
    print(reverse_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

    

if __name__=="__main__":
    main()