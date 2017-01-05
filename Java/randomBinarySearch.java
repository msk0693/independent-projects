/*
* 
* This program creates an array of random ints and lets the user
* search the array using binary search
* 
*/

import java.util.* ;
public class randomBinarySearch
{
 public static void main(String[] args)
  {

   Scanner in = new Scanner(System.in) ;
   Random rand = new Random();
   int array_size = 0 ;
   System.out.print("Enter size of array ") ;
   array_size = in.nextInt() ;
   int[] x = new int[array_size];
   int key = 0 ;
   

   for (int i = 0; i < x.length; i++)
   x[i] = rand.nextInt(100) + 1;
   Arrays.sort(x);
   System.out.println(Arrays.toString(x));

   System.out.println("Enter number to search in array above and recive index") ;
   key = in.nextInt() ;
   binarySearch(x, 0, x.length - 1, key) ;
   

 }

  public static void binarySearch(int[ ] m, int low, int high, int key)
   {
       int i = 0 ;
       i = ( low + high ) / 2 ;

       while((m[i] != key) && (low <= high))
       {
         if (m[i] > key)             
         {                                               
              high = i - 1;   
         }                                                             
              else                                                   
        {                                                        
              low = i + 1;    
        }

       i = (low + high) / 2;
     }
     if (low <= high)
     {
           System.out.println(key + " at position " + i);
     }
     else
     {
          System.out.println("number not found in array") ;
  }

}
}