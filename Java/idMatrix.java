/*
*
* This program has the user create a matrix of 1s and 0s then 
* displays the matrix and determines if it is an identity matrix
*
*/

import java.util.* ; 
public class idMatrix
{
 public static void main(String args [])
 {
  int n = 0 ;
  Scanner in = new Scanner(System.in) ;
  System.out.print("Enter dimensions of n x n array: ") ;
  n = in.nextInt() ;
  int [] [] x = new int[n][n] ;
  System.out.print("Fill array with 1 or 0\n") ;
  for (int r = 0 ; r < x.length ; r++)
  {
   for(int c = 0 ; c < x[0].length ; c++)
   {

    x[r][c] = in.nextInt() ;
 
    while (x[r][c] != 1 && x[r][c] != 0)
    {
     System.out.println("invalid option choose 1 or 0") ;
     x[r][c] = in.nextInt() ;
    }
   }
  }

  System.out.println("") ;

  display(x) ;
  System.out.println("Identity Matrix : " + check_id(x)) ;



 }
 public static boolean check_id(int [] [] a)
 {
   int count = 0 ;
  for (int r = 0 ; r < a.length ; r++ )
  {
    
   if (a[r][r] != 1) 
   {
    return false ;
   }

   for (int c = 0 ; c < a[0].length ; c++)
   {
     if(a[r][c] == 1)
     {
      count++ ;
     }
   }
  }
  if(count > a.length)
  {
   return false ;
  }
  return true ;
 }
 public static void display(int [] [] b )
 {
  for (int r = 0; r < b.length; r++) 
  {
     for (int c = 0; c < b[0].length; c++) 
     {

        System.out.print(b[r][c] + " ");
        
     }
    System.out.print("\n");
 }
  


 }
}